import numpy as np

# 1. dotProduct: is way of multiplying two vectors -> a1.b1 + a2.b2........
arr = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

dot = np.dot(arr, arr2)
print(dot)

# 2. matrix multiplication there are threee way of implemeent matrix mulitiplication

a = np.array([[1, 2],
              
              [4, 5]])

b = np.array([[7, 8],
              [10, 11]])

# first way
print(np.dot(a, b))

# second way
print(a @ b)

# third way
print(np.matmul(a, b))
    
# dot product in ML
x = np.array([1, 2])
w = np.array([4, 5])
b = 10

# y = w . x + b
y = np.dot(x, w) + b
print(y)

# usercase: linear regression, neural networks, embeddings, Batch proccessing