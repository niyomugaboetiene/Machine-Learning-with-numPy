# Simple linear reggression
import numpy as np
import matplotlib.pyplot as plt

# Generate dataset
X = np.arange(0, 10, 1)

y = 2 * X + 5 + np.random.randn(len(X))

X = np.array(X)
y = np.array(y)

w = 0.0
b = 0.0
learning_rate = 0.1
epochs = 1000

for i in range(epochs):
    y_pred = w * X + b
    dw = (-2 / len(X) * np.sum(X * (y - y_pred)))
    db = (-2 / len(X) * np.sum(y - y_pred))

    w -= learning_rate * dw
    b -= learning_rate * db


# Make prediction
X_plot = np.linspace(0, 10, 100)
y_plot = w * X_plot + b

plt.scatter(X, y, color='blue', label='data')
plt.plot(X_plot, y_plot, color='red', label='Prediction')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.legend()
plt.show()

hours = 7
predicted_score = w * hours + b
print(f"Predicted score for {hours} hours: {predicted_score:.2f}")