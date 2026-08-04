import numpy as np
# transpose -> is to transpose matrice by swaps its row and column (row become column and column become row)
# only affect 2D array
# ? usercase: is used to align shapes correctly 

A = np.array([[1, 2,],
              [3, 4]])

print("Original: ", A)

print("Transposed: ", A.T)

# np.reshape(rows, columns) changes the shape of array without changing its data
# usercase: in Matrix mulitiplication becuase it require compatible shape
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print("Reshaped into 2D", arr.reshape(2, 4))
# -1 tell python I dont know how may column is find it out
# col = 8 / 2 = 4 so the column will be 4 and two rows
# useful: when you don't one dimension in advance it caliculate missing dimension
print("Reshaped into 2D", arr.reshape(2, -1))

# changing 2D into 1D
print(A.reshape(-1))
