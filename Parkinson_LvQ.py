from random import randrange
import numpy as np
import pandas as pd


def LVQ_train(n_folds, n_codebooks, learn_rate, n_epochs):
	def CV_split(dataset, n_folds):
		dataset_split = list()
		dataset_copy = list(dataset)
		fold_size = int(len(dataset) / n_folds)
		for i in range(n_folds):
			fold = list()
			while len(fold) < fold_size:
				index = randrange(len(dataset_copy))
				fold.append(dataset_copy.pop(index))
			dataset_split.append(fold)
		return dataset_split

	def accuracy_metric(actual, predicted):
		correct = 0
		for i in range(len(actual)):
			if actual[i] == predicted[i]:
				correct += 1
		return correct / float(len(actual)) * 100.0

	def evaluate_algorithm(dataset, algorithm, n_folds, *args):
		folds = CV_split(dataset, n_folds)
		scores = list()
		for fold in folds:
			train_set = list(folds)
			#train_set.remove(fold)
			train_set = sum(train_set, [])
			test_set = list()
			for row in fold:
				row_copy = list(row)
				test_set.append(row_copy)
				row_copy[-1] = None
			predicted = algorithm(train_set, test_set, *args)
			actual = [row[-1] for row in fold]
			accuracy = accuracy_metric(actual, predicted)
			scores.append(accuracy)
		return scores

	def calc_distance(row1, row2):
		distance = 0.0
		for i in range(len(row1)-1):
			distance += (row1[i] - row2[i])**2
		return np.sqrt(distance)

# Locate the best matching unit / minimum unit
	def BMU(codebooks, test_row):
		distances = list()
		for codebook in codebooks:
			dist = calc_distance(codebook, test_row)
			distances.append((codebook, dist))
			distances.sort(key=lambda tup: tup[1])
		return distances[0][0]

# Make a prediction with codebook vectors
	def predict(codebooks, test_row):
		bmu = BMU(codebooks, test_row)
		return bmu[-1]

# Create a random codebook vector
	def random_codebook(train):
		n_records = len(train)
		n_features = len(train[0])
		codebook = [train[randrange(n_records)][i] for i in range(n_features)]
		return codebook

# Train a set of codebook vectors
	def train_codebooks(train, n_codebooks, lrate, epochs):
		codebooks = [random_codebook(train) for i in range(n_codebooks)]
		for epoch in range(epochs):
			rate = lrate * (1.0-(epoch/float(epochs)))
			for row in train:
				bmu = BMU(codebooks, row)
				for i in range(len(row)-1):
					error = row[i] - bmu[i]
					if bmu[-1] == row[-1]:
						bmu[i] += rate * error
					else:
						bmu[i] -= rate * error
		return codebooks

# LVQ Algorithm
	def LVQ(train, test, n_codebooks, lrate, epochs):
		codebooks = train_codebooks(train, n_codebooks, lrate, epochs)
		predictions = list()
		for row in test:
			output = predict(codebooks, row)
			predictions.append(output)
		return(predictions)

	dataframe = pd.read_csv("pd.csv")
	dataset = dataframe[['gender', 'PPE', 'DFA', 'RPDE',
               'ppq5Jitter', 'ddpJitter',
               'locAbsJitter', 'ddaShimmer',
               'apq3Shimmer', 'apq5Shimmer',
               'apq11Shimmer', 'GNE_mean','class']].to_numpy()
	
	scores = evaluate_algorithm(dataset, LVQ, n_folds, n_codebooks, learn_rate, n_epochs)
	print('Scores: %s' % scores)
	print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))