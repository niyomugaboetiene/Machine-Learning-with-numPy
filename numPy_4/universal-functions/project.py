import numpy as np
import matplotlib.pyplot as plt

X = np.array([1, 2, 3, 5, 6, 7])
Y = np.array([50, 55, 60, 65, 70, 75])

# preparing Z-normalzation
X_mean = np.min(X)
X_std = np.std(X)

# normalize Y usin Z-score formula
# z= x - mean / std
Y_mean = np.min(Y)
Y_std = np.std(Y)

# prepare data for ML and algorithm
print("X_mean:", X_mean, "X_std", X_std)
print("Y_mean", Y_mean, "Y_std", Y_std)

# z= x - mean / std
x_normalized = (X - X_mean) / X_std;
Y_normalized = (Y - Y_mean) / Y_std;

print("Mean of X_normalized", np.mean(x_normalized))
print("std of X_normalized", np.std(x_normalized))

print("Mean of y_normalized", np.mean(Y_normalized))
print("std y_normalized", np.std(Y_normalized))

plt.scatter(x_normalized, Y_normalized, color='blue', label='Normalized Data')
plt.xlabel('Y_normalized')
plt.ylabel('y_normalized')
plt.title('Z-score Normalization')
plt.legend()
plt.show()