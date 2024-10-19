import numpy as np

# Generate random normal data
np.random.seed(42)
data = np.random.normal(loc=0, scale=1, size=10)  # Small dataset for manual calculations

# Step 1: Calculate Mean (First Moment)
mean = np.sum(data) / len(data)
print(f"Mean (1st moment): {mean}")

# Step 2: Calculate Variance (Second Moment)
variance = np.sum((data - mean) ** 2) / len(data)
print(f"Variance (2nd moment): {variance}")

# Step 3: Calculate Third Moment
third_moment = np.sum((data - mean) ** 3) / len(data)
print(f"Third Moment: {third_moment}")

# Step 4: Calculate Fourth Moment
fourth_moment = np.sum((data - mean) ** 4) / len(data)
print(f"Fourth Moment: {fourth_moment}")

# Step 5: Calculate Skewness
std_dev = np.sqrt(variance)  # Standard deviation
skewness = np.sum(((data - mean) / std_dev) ** 3) / len(data)
print(f"Skewness: {skewness}")

# Step 6: Calculate Kurtosis
kurtosis = np.sum(((data - mean) / std_dev) ** 4) / len(data)
excess_kurtosis = kurtosis - 3  # Subtract 3 to get excess kurtosis
print(f"Kurtosis: {kurtosis}")
print(f"Excess Kurtosis: {excess_kurtosis}")
