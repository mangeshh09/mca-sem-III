import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (You can load your own dataset, here we'll generate some data similar to 'tips' dataset)
data = {
    'total_bill': np.random.uniform(10, 50, 100),
    'tip': np.random.uniform(1, 10, 100),
    'size': np.random.randint(1, 6, 100)
}
df = pd.DataFrame(data)

# a) Find Covariance Matrix
cov_matrix = df.cov()
print("Covariance Matrix:")
print(cov_matrix)

# b) Find Correlation Matrix
corr_matrix = df.corr()
print("\nCorrelation Matrix:")
print(corr_matrix)

# Plotting the correlation matrix using Matplotlib (without seaborn)
plt.figure(figsize=(8, 6))

# Create a heatmap manually
plt.imshow(corr_matrix, cmap='coolwarm', interpolation='nearest')

# Add a color bar
plt.colorbar()

# Add tick marks and labels
plt.xticks(np.arange(len(corr_matrix.columns)), corr_matrix.columns, rotation=45)
plt.yticks(np.arange(len(corr_matrix.columns)), corr_matrix.columns)

# Annotate the matrix with the correlation values
for i in range(len(corr_matrix.columns)):
    for j in range(len(corr_matrix.columns)):
        plt.text(j, i, f'{corr_matrix.iloc[i, j]:.2f}', ha='center', va='center', color='black')

plt.title("Correlation Matrix Heatmap")
plt.tight_layout()
plt.show()
