import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# reading the csv source
df = pd.read_csv('park.csv')

features = df[['MDVP:Jitter(Abs)', 'Jitter:DDP', 'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 'RPDE', 'DFA', 'D2', 'PPE']]
X = features.to_numpy()
Y = df[['status']].to_numpy().reshape(-1)


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=30)
C = np.linspace(1,100,200).reshape(-1)
accuracy = []

for c in C:
    SVM = SVC(kernel='linear', C=c, random_state=30)
    SVM.fit(X_train, Y_train)
    Y_predict = SVM.predict(X_test)
    accuracy.append(accuracy_score(Y_test, Y_predict)*100)

plt.plot(C, accuracy)
plt.xlabel("Value of C :")
plt.ylabel("Accuracy in % :")
plt.show()
accuracy.clear()
#print(accuracy)

