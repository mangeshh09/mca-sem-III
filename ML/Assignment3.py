import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the dataset
column_names = ['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms', 'Area Population', 'Price', 'Address']
bos1 = pd.read_csv('housing1.csv')

# Check the shape and first few rows of the dataset
print("Shape of dataset:", bos1.shape)
print("First few rows of the dataset:\n", bos1.head())

# Preprocessing the data: Removing NaN values
bos1 = bos1.dropna()

# Check the shape after dropping NaN values
print("Shape after dropping NaN values:", bos1.shape)

# Ensure the data has been loaded correctly and is not empty
if bos1.empty:
    raise ValueError("The dataset is empty. Please check the file path and format.")

# Define features (X) and target (Y)
# Features: All columns except 'Price' and 'Address'
# Target: 'Price'
X = bos1[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms', 'Area Population']]
Y = bos1['Price']

# Ensure the features and target arrays are not empty
if X.empty or Y.empty:
    raise ValueError("Feature or target arrays are empty. Please check the data loading process.")

# Splitting the data into training and testing sets (70% training, 30% testing)
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.30, random_state=5)

# Using Linear Regression Model
lr = LinearRegression()
# Train the model on the training data
lr.fit(x_train, y_train)
# Predict the testing data so that we can later evaluate the model
pred_lr = lr.predict(x_test)

# Model Evaluation
# Mean squared error (MSE) for linear regression
mse_lr = mean_squared_error(y_test, pred_lr)

# Root mean squared error (RMSE)
rmse_lr = np.sqrt(mse_lr)
print("Error for Linear Regression (RMSE) = {:.2f}".format(rmse_lr))
