import numpy as np
from scipy.stats import skew, kurtosis

# Example data: you can replace this with real-time data
data = np.random.normal(loc=0, scale=1, size=1000)  # Random normal distribution

# Calculate moments
mean = np.mean(data)  # First moment
variance = np.var(data)  # Second moment (variance)
third_moment = np.mean((data - mean) ** 3)  # Third moment
fourth_moment = np.mean((data - mean) ** 4)  # Fourth moment

# Calculate skewness and kurtosis
skewness = skew(data)
kurt = kurtosis(data, fisher=False)  # Fisher=False gives the "excess" kurtosis

# Print results
print(f"Mean (1st moment): {mean}")
print(f"Variance (2nd moment): {variance}")
print(f"Third Moment: {third_moment}")
print(f"Fourth Moment: {fourth_moment}")
print(f"Skewness: {skewness}")
print(f"Kurtosis: {kurt}")
