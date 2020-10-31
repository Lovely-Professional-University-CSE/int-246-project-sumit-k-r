import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


def sigmoid(x):
    return 1/(1+np.exp(-x))

dataframe = pd.read_csv("pd.csv")

features = dataframe[['gender', 'PPE', 'DFA',
                      'RPDE','ppq5Jitter',
                      'ddpJitter','locAbsJitter',
                      'ddaShimmer','apq3Shimmer',
                      'apq5Shimmer','apq11Shimmer',
                      'GNE_mean']]

X = features.to_numpy()
Y = dataframe[['class']].to_numpy().reshape(-1)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4, random_state=40)

#Random Weights
Weights = np.random.uniform(size=(X_train.shape[1]))
epochs = 50
bias = 0.05
l_rate = 0.03
threshold = 0.5

def classifier(x, threshold):
    return 1 if x>=threshold else 0

for epoch in range(epochs):
    for i in range(X_train.shape[0]):
        y = np.dot(X_train[i],Weights) + bias
        yin = sigmoid(y)
        yin = classifier(yin,threshold)  
        if yin == Y_train[i]:
            Weights+= l_rate*epoch*X_train[i]
            bias+=l_rate*epoch
        # print("Expected : ",Y_train[i],"Predicted : ",yin)

correct =0
for i in range(X_test.shape[0]):
    y = np.dot(X_test[i],Weights)
    yin = sigmoid(yin)
    yin = classifier(yin,threshold)
    if(yin == Y_test[i]):
        correct+=1

print("Accuracy : ",end="")
print('%.2f'%((float(correct)/float(X_test.shape[0]))*100.0),"%")