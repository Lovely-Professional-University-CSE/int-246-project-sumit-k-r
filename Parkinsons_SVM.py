import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

df = pd.read_csv('pd.csv')
# df.head()
features = df[['gender', 'PPE', 'DFA', 'RPDE',
               'ppq5Jitter', 'ddpJitter',
               'locAbsJitter', 'ddaShimmer',
               'apq3Shimmer', 'apq5Shimmer',
               'apq11Shimmer', 'GNE_mean']]

X = features.to_numpy()
Y = df[['class']].to_numpy().reshape(-1)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=40)

C = np.linspace(1, 50, 50).reshape(-1)
accuracy_linear = []
accuracy_poly = []
accuracy_rbf = []


for c in C:
    SVM = SVC(kernel='linear', C=c, random_state=40)
    SVM.fit(X_train, Y_train)
    Y_predict = SVM.predict(X_test)
    accuracy_linear.append(accuracy_score(Y_test, Y_predict)*100)
for c in C:
    SVM = SVC(kernel='poly', C=c, random_state=40)
    SVM.fit(X_train, Y_train)
    Y_predict = SVM.predict(X_test)
    accuracy_poly.append(accuracy_score(Y_test, Y_predict)*100)
for c in C:
    SVM = SVC(kernel='rbf', C=c, random_state=40)
    SVM.fit(X_train, Y_train)
    Y_predict = SVM.predict(X_test)
    accuracy_rbf.append(accuracy_score(Y_test, Y_predict)*100)

sns.set_theme()
plt.plot(C, accuracy_linear, label="Linear")
plt.plot(C, accuracy_poly, label="Poly")
plt.plot(C, accuracy_rbf, label="RBF")
plt.xlabel("Value of C :")
plt.ylabel("Accuracy in % :")
plt.title("SVC with random state = 40")
plt.legend()
plt.show()
print("Mean accuracy of Kernals : ")
print("Linear : ", np.mean(accuracy_linear))
print("RBF : ", np.mean(accuracy_rbf))
print("Poly : ", np.mean(accuracy_poly))
