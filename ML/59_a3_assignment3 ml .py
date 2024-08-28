import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Column names for the dataset
column_names = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms',
                 'population', 'households', 'median_income', 'median_house_value']

# Path to the dataset
file_path = r'F:\60_A3_SIDDHESH DBMS ASSIGNMENT\MACHINE LEARNING\housing.csv'

# Load the dataset
bos1 = pd.read_csv(file_path, delimiter=r"\s+", names=column_names, skiprows=1)

# Drop rows with missing values
bos1 = bos1.dropna()

# Print the data types before conversion
print("Data types before cleaning:")
print(bos1.dtypes)

# Convert non-numeric columns to numeric (coerce errors to NaN)
for col in ['households', 'median_income', 'median_house_value']:
    bos1[col] = pd.to_numeric(bos1[col], errors='coerce')

# Drop rows with NaN values after conversion
bos1 = bos1.dropna()

# Print the first few rows and data types after conversion
print("Data preview after cleaning:")
print(bos1.head())
print("Data types after cleaning:")
print(bos1.dtypes)

# Define feature variables (X) and target variable (Y)
X = bos1.drop('median_house_value', axis=1).values
Y = bos1['median_house_value'].values

# Check the shape of X and Y to ensure there are samples
print(f"Shape of X: {X.shape}")
print(f"Shape of Y: {Y.shape}")

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.30, random_state=5)

# Initialize and train the Linear Regression model
lr = LinearRegression()
lr.fit(x_train, y_train)

# Predict the target values for the test set
pred_lr = lr.predict(x_test)

# Model Evaluation: Calculate the Root Mean Squared Error (RMSE)
mse_lr = mean_squared_error(y_test, pred_lr, squared=False)
print("Error for Linear Regression (RMSE) = {}".format(mse_lr))
