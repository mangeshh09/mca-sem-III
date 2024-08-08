import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn import metrics
'''
Imports necessary libraries:
numpy and pandas are used for data manipulation.
matplotlib.pyplot is used for plotting.
load_iris from sklearn.datasets loads the Iris dataset.
StandardScaler standardizes features by removing the mean and scaling to unit variance.
PCA from sklearn.decomposition performs Principal Component Analysis.
metrics is imported but not used in this snippet.
'''

# Load the Iris dataset
data = load_iris()  #load_iris() loads the dataset and returns a dictionary-like object.
X = data.data  #X contains the feature data (e.g., sepal length, sepal width).
y = data.target  #y contains the target labels (species of iris).
target_names = data.target_names   #target_names holds the names of the iris species.

# Standardize the data
scaler = StandardScaler()   #StandardScaler() creates an instance of the scaler.
X_standardized = scaler.fit_transform(X)  #fit_transform(X) standardizes X by removing the mean and scaling to unit variance, resulting in X_standardized.

# Initialize PCA
pca = PCA() #Creates an instance of PCA without specifying the number of components.

# Fit PCA on the standardized data
pca.fit(X_standardized)  #Computes the principal components and the explained variance from the standardized data.

# Calculate the cumulative explained variance ratio
explained_variance_ratio = pca.explained_variance_ratio_  #explained_variance_ratio_ contains the proportion of variance explained by each principal component.
cumulative_explained_variance_ratio = np.cumsum(explained_variance_ratio)  #np.cumsum(explained_variance_ratio) computes the cumulative sum of these ratios to understand how much variance is explained by the first n components.

# Determine the number of components needed to retain at least 95% variance
n_components = np.argmax(cumulative_explained_variance_ratio >= 0.95) + 1
#np.argmax(cumulative_explained_variance_ratio >= 0.95) finds the index of the first component where the cumulative explained variance reaches or exceeds 95%.
#+1 adjusts the index to account for zero-based indexing, giving the number of components needed.

# Transform the data to the new feature space
pca = PCA(n_components=n_components) #PCA(n_components=n_components) creates a PCA instance with the calculated number of components.
X_pca = pca.fit_transform(X_standardized) #fit_transform(X_standardized) projects the data onto the selected principal components, resulting in X_pca.

# Output the results
print(f'Number of components selected: {n_components}')
print(f'Explained variance ratio of each component: {explained_variance_ratio}')
print(f'Cumulative explained variance ratio: {cumulative_explained_variance_ratio}')

# Plot the results
plt.figure(figsize=(10, 7))
colors = ['navy', 'turquoise', 'darkorange']
for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(X_pca[y == i, 0], X_pca[y == i, 1], color=color, label=target_name)
plt.title(f'PCA of Iris Dataset\nComponents: {n_components}')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend(loc='best')
plt.grid()
plt.show()

'''
plt.figure(figsize=(10, 7)) creates a figure with a specified size.
colors defines a list of colors for different iris species.
The for loop creates scatter plots for each class in different colors.
X_pca[y == i, 0] and X_pca[y == i, 1] select the first and second principal components for each class.
color and label differentiate the classes in the plot.
plt.title() sets the title of the plot.
plt.xlabel() and plt.ylabel() label the axes.
plt.legend() adds a legend to the plot.
plt.grid() enables the grid.
plt.show() displays the plot.
'''
