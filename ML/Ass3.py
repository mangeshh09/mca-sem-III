import numpy as np
import matplotlib.pyplot as plt

# Define the data directly
hours = np.array([10, 9, 2, 15, 10, 16, 11, 16])
risk_scores = np.array([95, 80, 10, 50, 45, 98, 38, 93])

# Calculate the means
mean_x = np.mean(hours)
mean_y = np.mean(risk_scores)

# Calculate the slope (m) and intercept (b)
numerator = np.sum((hours - mean_x) * (risk_scores - mean_y))
denominator = np.sum((hours - mean_x) ** 2)
m = numerator / denominator
b = mean_y - m * mean_x

# Print the slope and intercept
print(f"Slope (m): {m}")
print(f"Intercept (b): {b}")

# Define the best fit line
def predict(x):
    return m * x + b

# Predict the risk score for 20 hours
hours_to_predict = 20
predicted_risk = predict(hours_to_predict)
print(f"Predicted risk score for {hours_to_predict} hours: {predicted_risk}")

# Plot the data and the best fit line
plt.scatter(hours, risk_scores, color='blue', label='Data Points')
plt.plot(hours, predict(hours), color='red', label='Best Fit Line')
plt.xlabel('Hours Spent Driving')
plt.ylabel('Risk Score')
plt.title('Linear Regression')
plt.legend()
plt.grid(True)
plt.show()
