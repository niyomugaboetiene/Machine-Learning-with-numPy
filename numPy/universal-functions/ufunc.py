# universal function(ufuncs) is function that operate wise-element on darrays
# * they are fast and applied to the whole array at once
# * ex: np.add, np.subtract, np.exp, np.log, np.sqrt etc...

# 1. np.exp() -> computes an exponential of each element in the input array
# where e = 2.718 (Euler's number)
# usercase: softmax function  convert secores into probabilities
import numpy as np

# single value 
print(np.exp(1)) # e^1
print(np.exp(2)) # e^2

# array of numbers
array = np.array([1, 2, 3, 4, 5])
print(np.exp(array)) # apply exponential to each item in the array

# simple softmax function
score = np.array([2.0, 5.0, 6.0])
exp_secore = np.exp(score) # to male all number positive becuase probability can not be less than 0
probabilites = exp_secore / np.sum(np.exp(score))
print(probabilites)

# Gradient Descent
# row output of model
# usercase: image classification, text calassification, 
scores = np.array([1000, 1001, 1002])
# the why we shifted by max is to make numbers smaller which is better for computation
shifted_scores = scores - max(scores)
# make all numbers positive
exp_secores = np.exp(shifted_scores)
# find probabilities
probs = exp_secores / np.sum(exp_secores);

print(probs)

# 2. np.log(x) means computes natural logarithm of x
# means to what should be e raised to get x
# usercase: compression it can be used to shrink large numbers into smaller manageable numbers
print(np.log(1)) # 0 because e^0 = 1
print(np.log(np.e))  # because e^1 = e

income = np.array([1000, 2000, 3000])
log_income = np.log(income) # it return the large number into smaller number
print(log_income)

# measure how well the predicted probabilities match the true labales
# actual label of my data 1 means the positive and 0 means the negative
y_true = np.array([1, 0, 1])
# predicted probabilite from my model
# 0.9 means 90%, ...
y_pred = np.array([0.9, 0.2, 0.8])
# ? formual: −[y⋅log(y^​)+(1−y)⋅log(1−y^​)]
# y^ is y_pred, and y is y_true
loss =  -(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
print(loss)
# how log works
arrays = np.array([1, 10, 5])
print(np.log(arrays)) 
# it checks how power needed to raise e to get each number
# ex: to get 10 which power will be needed
# e ^ 1 = 2.7 too small
# e ^2 = 7.38
# e ^ 2.3 = 9.9 very close to 10


# np.sqrt() -> means square root of each element in array x
# ? usercase: distance calicultaion, standard deviation  formula: d=(x1​−x2​)2+(y1​−y2​)2
sqrt = np.array([1, 2, 3, 4, 5, 6])
print("Sqaure root", np.sqrt(sqrt));

# distance calicultaion
point1 = np.array([3, 4])
point2 = np.array([5 ,6])
#   subtract the vectors [3, 4] - [5, 6] = [3 - 5, 4 - 6] = [-2, -2]
# square the diffrence [-2, -2] ** 2 = [4, 4]
# find sum  = 4 + 4 = 8
# find square root = np.sqrt(8) = 2.828
dist = np.sqrt(np.sum((point1 - point2) ** 2))
print(dist)

# ? min and max functions 
# np.min() -> return the smallest value in the array
# np.max() -> return the largest value in the array
# usercase: feature sclaring and normalization, Data anlysis

arr = [1, 2, 3, 4, 5]
print("Max value", np.max(arr))
print("Min value", np.min(arr))