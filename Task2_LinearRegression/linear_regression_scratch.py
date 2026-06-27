import numpy as np
import matplotlib.pyplot as plt

# Step 1: Dataset Creation
X = np.array([1,2,3,4,5,6,7,8,9,10], dtype=float) # Study Hours
y = np.array([35,45,50,55,65,70,75,80,85,95], dtype=float) # Scores

# Step 2: Calculate Slope
x_mean, y_mean = np.mean(X), np.mean(y)
slope = np.sum((X - x_mean) * (y - y_mean)) / np.sum((X - x_mean)**2)

# Step 3: Calculate Intercept
intercept = y_mean - slope * x_mean

# Step 4: Prediction
y_pred = slope * X + intercept

# Step 5: Mean Squared Error
mse = np.mean((y - y_pred)**2)

print(f"Slope (m) : {slope:.4f}")
print(f"Intercept (b) : {intercept:.4f}")
print(f"Regression Line : y = {slope:.4f}x + {intercept:.4f}")
print(f"Predicted Scores: {np.round(y_pred, 2).tolist()}")
print(f"MSE : {mse:.4f}")
print(f"RMSE : {np.sqrt(mse):.4f}")

# Visualization
plt.scatter(X, y, color='blue', label='Actual Data Points')
plt.plot(X, y_pred, color='red', label=f'Regression Line: y = {slope:.2f}x + {intercept:.2f}')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score')
plt.title('Linear Regression from Scratch\nStudy Hours vs Exam Score')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('linear_regression_output.png')
plt.show()
