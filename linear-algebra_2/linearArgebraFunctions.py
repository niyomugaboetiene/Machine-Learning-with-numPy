# find inverse of square matrix
# usercase: in linerar regression when computing with weights using noraml equation
# allows to find original weight or solution that best fits the data
# ? the inverse of 2 is 1/2
import numpy as np

A = np.array([[1, 2],
              [4, 5]])

A_inv = np.linalg.inv(A);9

print(A @ A_inv);

# np.lin.linalg.det () -> determinant is single number that gives you info about matrice
# measure how it is invertable or scalable
print(np.linalg.det(A))
B = np.array ([[2, 5],
               [6, 8]])
print(np.linalg.det(B)) 
print(np.linalg.inv(B))

values, vectors = np.linalg.eig(B)
print("Values:", values)
print("Vectors", vectors)

# np.linalg.norm() -> measure how long vector is
vector = np.array([2, 3])
print(np.linalg.norm(vector))
# It comes from the Pythagoras theorem:

# distance btn data point
vect2 = np.array([4, 5])
distance = np.linalg.norm(vector - vect2)
print(distance)

A = np.array([[3, 4],
              [6, 7]])

B = np.array([1, 2])
solution = np.linalg.solve(A, B)
print(solution)
# 2x+y=5
# 5𝑥+3𝑦=13

X = np.array([[1, 1],
              [1, 2],
              [1, 3]]) # features

y = np.array([1, 2, 3]) # targeted

A = X.T @ X # matrix multiplication
b = X.T @ y # vector multiplication
w = np.linalg.solve(A, b)
print("Weight: ", w);