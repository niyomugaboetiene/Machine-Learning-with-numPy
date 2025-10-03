import numpy as np

# converting data btn range of 0 and 1 
# which help to train data faster, prevent numeric instability

y = np.array([1, 2, 3, 5])
x = np.array([15, 20, 25, 30, 35])

x_axis = (x - np.min(x)) / (np.max(x) - np.min(x))
y_axis = (y - np.min(y)) / (np.max(y) - np.min(y))

print("X_scaled", x_axis)
print("Y_scaled", y_axis)