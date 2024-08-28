import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsRegressor
from sklearn.impute import SimpleImputer

# Load dataset
column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE',
                'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
df = pd.read_csv('BostonHousing.csv', header=None, names=column_names)

# Drop rows with missing values
df = df.dropna()

# Separate features and target variable
X = df.iloc[:, :-1].values
Y = df['MEDV'].values

# Convert to numeric (just in case there are any non-numeric values)
X = pd.DataFrame(X).apply(pd.to_numeric, errors='coerce').values
Y = pd.Series(Y).apply(pd.to_numeric, errors='coerce').values

# Impute missing values (if any)
imputer = SimpleImputer(strategy='mean')
X = imputer.fit_transform(X)
Y = imputer.fit_transform(Y.reshape(-1, 1)).ravel()

# Split dataset into training and test sets
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=5)

# Initialize KNN with k=5
knn = KNeighborsRegressor(n_neighbors=5)
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)

# Print Mean Squared Error for k=5
print("Mean squared error for k=5: %.2f" % mean_squared_error(y_test, y_pred))

# Find the best k
best_k = 0
best_rmse = float('inf')
for i in range(1, 50):
    knn = KNeighborsRegressor(n_neighbors=i)
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    print(f"RMSE for k = {i}: {rmse:.2f}")
    if rmse < best_rmse:
        best_rmse = rmse
        best_k = i

print(f"Best k = {best_k} with RMSE = {best_rmse:.2f}")

# Print RMSE for the best k
print(f"RMSE for KNN Algorithm: {best_rmse:.2f}")
