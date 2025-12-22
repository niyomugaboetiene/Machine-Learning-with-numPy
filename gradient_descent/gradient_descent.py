import numpy as np
# Goal:

# To find the best-fit straight line:
# 𝑦=mx+b
# Gradient descent learns the values of:
# m → slope
# b → intercept
def gradient_descent(x, y):
    # Start with slope m = 0
    # Start with intercept b = 0
    m_curr = b_curr = 0
    # iteration → number of times the model updates parameters
    iteration = 1000
    # n → number of data points
    n = len(x)
    # learning_rate → step size (how fast parameters change)
    learning_rate = 0.08
  
    for i in range(iteration):
        # y=mx+b
        y_predicted = m_curr * x + b_curr
        # If prediction is too small → error is positive
        # If prediction is too big → error is negative
        # md tells us how much and in which direction the slope m is wrong
        md = -(2/n) * sum(x * (y - y_predicted))
        # bd tells us how much and in which direction the intercept b is wrong
        bd = -(2/n) * sum(y - y_predicted)
        # cost = 1/n(sum(y - y_predicted)**2)
        cost = (1/n) * sum([val ** 2 for val in (y - y_predicted)])
        # m = m - learning_rate * m derivative
        # new value=old value−(learning rate×gradient)
        m_curr = m_curr - learning_rate * md
        # m = b - learning_rate * b derivative
        b_curr = b_curr - learning_rate * bd
        print("m {} b {}, cost {}, iteration {}".format(m_curr, b_curr, cost , i))

  
x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])

gradient_descent(x, y)