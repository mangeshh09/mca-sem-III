# importing all the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Social_Network_Ads.csv')
print(dataset.head())

# Filtering out columns to retain age and salary columns
X = dataset.iloc[:,[2,3]]. values
Y = dataset.iloc[:,4].values

# Data split for training and testing (75/25)
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.25, random_state = 0)

#Scaling using standard scalar for Normal Distribution
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#Building the model using RBF kernel
from sklearn.svm import SVC
classifier_rbf = SVC(kernel = 'rbf', random_state = 0)
classifier_rbf.fit(X_train, Y_train)
Y_pred_rbf = classifier_rbf.predict(X_test)

#Printing the confusion matrix
from sklearn.metrics import confusion_matrix
cm_rbf = confusion_matrix(Y_test, Y_pred_rbf)
print(cm_rbf)

# Classification Report
from sklearn.metrics import classification_report
class_report_rbf = classification_report(Y_test, Y_pred_rbf)
print(class_report_rbf)
