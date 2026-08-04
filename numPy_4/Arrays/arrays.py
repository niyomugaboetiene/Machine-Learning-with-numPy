import numpy as np

# np.arrays is function which helps to create arrays in numPy
# 1D Array think like single feature in ML
a = np.array([1, 2, 3])
print(a) # print value of a
print(type(a)) # print type of a ndarray
print(a.shape) # print shape of a  3 

# 2D arrays used to represent Dataset, with rows = samples and colums = features 
# example student marks in three subject
b = np.array([[1, 2, 3],
             [4, 5, 6]])
print(b)
print(b.shape)

# 3D arrays used in DL like images , Audios, Video
# example color image is stored in 3D (height, width, channel)

c = np.array([[
    [1, 2], [3, 4],
    [5, 6], [7, 8]
]])

print(c)
print(c.shape)

# Forcing Datatype used in training model that require specific datatype like float32 for neural networks
d = np.array([1.2, 2.2, 3.4], dtype=np.int32)
print(d)
print(d.shape)

# nested arrays:  it is used to slice dataset into row: samples and colums: features
data = np.array([[10, 20], [30, 40], [50, 60]])
print(data)
print(data[0])
print(data[:,1]) # : means all rows, 1: means on the second column means it fetch all rows in the second column

# arange is used to create evenly values within specified interval
# syntax: np.range([start, ], stop, [step, ]dtype=None)
# it is similar to range but it supports float
# in ML generate generate datasets, grid, for testing models

r = np.arange(5)
print(r)

f = np.arange(8, 0, -2)
print(f)

# linespace is the same as arrange but it is used to display specific numbers within specified interval
# syntax: ([start, stop, num, endpoint, retstep])
# num is number being displayed within interval
# endpoint by defauilt is true means also the last number inclueded if false excluded
# retspet display spacing btn numbers as well
l = np.linspace(0, 10, 5) # display five numbers within 10 interal
print(l)

ls = np.linspace(0 , 10, 5, endpoint=False)
print(ls)

arr, step = np.linspace(0, 10 ,5, retstep=True)
print("Array", arr)
print("Step between each numbers", step)