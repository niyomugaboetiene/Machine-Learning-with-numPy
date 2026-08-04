# Array initialization

import numpy as np

# 1 np.zeros(row, colums) -> is used to initialize array with zero value
# produce array which has zero values 
# usercase: in ML is used to initialize weight to zero value in neular network
# represent empy array before filling data
zero = np.zeros((2, 3))
print(zero)

# 2. np.ones(rows, colums) -> create array field with ones
# usercaes: initialize bias in neural networks, quick testing algorithm
ones = np.ones((2, 3) , dtype=int)
print(ones)


# 3 np.eye() -> is used to create indentical matrix
# usercase: linear algebra used in ML optimization
# solving system equations
matrix = np.eye((4))
print(matrix)

# arrays attributes
# 1. np.shape -> returns dimensions of arrays as turple, returns rows and columns as turple (rows, colums)
# usecase in ML: Input features often has a shape (n_sample, n_features), checks if matrix are compatible for mulitiplication
shapes = np.array([[1, 2, 3], [4, 5, 6]])
print(shapes.shape)

# 2. np.ndim() -> retuns dimension of array like 1D, 2D, 3D
# usercase: in ML 1D -> vector (weight, bias), ensure if your model input is correct
# 2D -> matrix datasets
# 3D -> tensors (images, videos, ..)

dimension = np.array([[1,2,3], [1,2,3]])
print(dimension.ndim)

# 3. np.size -> returns total number of element in the array
# usercase in ML: it tells how much datta you're handling
size = np.array([[1,2, 3, 4], [5, 6, 7, 8]])
print(size.size)

# 4. np.dtype -> returns data type of the elements in the array
# usercase: ensure your data and weight is in the right type
datatype = np.array([1,2, 3], dtype=float)
print(datatype.dtype)

# Indexing and slicing 
# 1. indexing -> choosing specific elements in the array
# 1D example
array = [10, 20 ,30, 40, 50]
# indexing
print(array[0]) # first element
print(array[-1]) # last element

# slicing
print(array[0:3]) # from index 0 up to index 3
print(array[:3]) # include first three elements
print(array[::3]) # include first second element  jump every items on thrid index

# 2D example
# indexing
array2 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(array2[0, 0]) # row on index 0 and col on index 0
print(array2[1, 1])
# slicing
print(array2[0, :]) # row 0 and all colums
print(array2[:, 0]) # all rows colum 0
print(array2[:, 1])

# 3D example
array3 = np.array([
    # gets every second elements in last row of all blocks

                   [[1, 2, 3],
                   [4, 5, 6]], # block 1
                    [
                        [7, 8, 9], 
                        [10, 11, 12]
                    ],  # block 2
                    [
                        [13, 14, 15],
                        [16, 17, 18]
                    ], # block 3
                  ])
 
print("shape is", array3.shape)  # (3:2:3) 1 -> there are only one big block
                                  # syntax: block, rows in each block, columns in each row 
                                  # 4 ->  there are four colums
                                  #  2 -> each column contain 2 elements 
# indexing
# syntax: block_index, row_index, column_index
print(array3[0,0,1]) # 2 in block 1
print(array3[1,1,2])


# Slicing syntax: start_block:end_block, start_row:end_row, start_column:end_column
# start:end are indexes
# : all elements belong to that dimension

# example get first two block with all columns and rows
print(array3[0:1, :, :]) # 0:1 0 -> block 0 & 1, : -> all rows, : -> all columns
# get all blocks with its first row
print(array3[0:3, 0, :]) 
# get last column of all rows in second block
print("lat one",array3[1, :, 2])
print("new one", array3[2, :, 1])

# get first 2 rows of last 2 blocks , first 2 columns
print(array3[1:, 0:2, 0:2])
# 1:0 takes last two blocks, 0:2 -> first two rows, 0:2 first two columns

# gets every second elements in last row of all blocks
print(array3[:, 1, ::2])
# ::: -> start, stop, end
# ::2 means : start from index 0 up to last index and skip 1 elements
# indexing and slicing can be applied in ML for selecting samples, Test data

# Boolean indexing is way of pick elements in the array based on specific condition
# usercase -> handling missing or invalid data in ML
boolean = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# * create boolean mask to print true, false to each elemnt based on condition
# ? create boolean mask to print true, false to each elemnt based on condition
# ! create boolean mask to print true, false to each elemnt based on condition
# create boolean mask to print true, false to each elemnt based on condition
mask = boolean > 5
print(mask)

# pick elements instead of returning true or false
element = boolean[boolean > 5]
print(element) 

# multiple conditions
print(array3[(array3 > 3) & (array3 < 6)])