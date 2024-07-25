#!pip install scikit-learn pandas numpy dtale notebook
import pandas as pd
import numpy as np
#import dtale
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing  import StandardScaler

data={'  Region' : ['India','Brazil','USA','Brazil','USA','India','Brazil','India','nan','India'],
      '  Age':['49','32','35','43','45','40','nan','53','55','42'],
      '   Income':['86400','57600','64800','73200','nan','69600','62400','94800','99600','80400'],
      '    Online Shopper':['No','Yes','No','No','Yes','Yes','No','Yes','No','Yes']
      }
dataset=pd.DataFrame(data)

print(dataset)

X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:, -1].values

print(X)

print(Y)

imputer = SimpleImputer(missing_values=np.nan,strategy="mean")
imputer = imputer.fit(X[:,1:])
X[:,1:] = imputer.transform(X[:,1:])

print(X)

labelencoder_X = LabelEncoder()
X[:,0]=labelencoder_X.fit_transform(X[:,0])
ct=ColumnTransformer([("Region",OneHotEncoder(),[0])],remainder='passthrough')
X=ct.fit_transform(X)
labelencoder_Y=LabelEncoder()
Y=labelencoder_Y.fit_transform(Y)

print(X)
print(Y)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=0)

print(X_train)

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

print(X_train)