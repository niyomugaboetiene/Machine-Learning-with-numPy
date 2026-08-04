# matplotlib is library which used in ML for Data visualization which allows for better learning and data underdstanding!
import matplotlib.pyplot as plt
import numpy as np

# a = np.array([1, 2, 3, 4, 5, 6])
# b = [2, 4, 6, 8, 10, 12]

# # 1. plt.plot() -> create line which links a and b used for show relationships btn data
# # linestyle -> is used to control tyoe of line as dotted .., dashed --, -. dotdasheed, dottedline :
# # marker -> is used to show point at each value adds point where values meets
# # some marker ex: -> o circle, s square, ^ triange, * star 
# plt.plot(a, b, linestyle="--", marker="o")
# plt.title("Line-chart Example") # title of our chart
# plt.xlabel("X-axis") # label in X axis 
# plt.ylabel("Y-axis") # Y axis label
# plt.show() # shows the graph

# 2. plt.bar() -> used for compare categories
categories = ["Banana", "Apples", "Cherries"]
price = [10, 20, 30]

plt.bar(categories, price)
plt.title("Bar chart Example")
plt.xlabel("Fruits")
plt.ylabel("Price")
plt.show()

# 3. plt.histogram() -> is used for data distribution
# how it works it find minimum and maximum
# data = [20, 87, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27]
# # bins divide the whole range into into 5 intervals
# # find bin width => max - min / nbr of bins
# # create bin range min + bin range do it until you exceed to max number 
# plt.hist(data, bins=5, color="orange")
# plt.title("Histogram Example")
# plt.xlabel("Range")
# plt.ylabel("Frequency")
# plt.show()

# 4. plt.scatter -> is used to show also relationship  study hours vs exam scores
# it uses dot
# hour = [5, 7, 8, 7, 6, 9, 5]
# scores = [99, 86, 87, 88, 100, 86, 103]

# plt.scatter(hour, scores)
# plt.title("Scatter chart example")
# plt.xlabel("X-axis")
# plt.ylabel("Y-Axis")
# plt.show()

# legend -> is used to label your line when multiple port are on the same figure
# how it works -> you must provide labels inside plot() and call .legend() to display them

# y1 = a**2
# y2 = a**1.5
# plt.plot(a, y1, label="x squared", color="blue")
# plt.plot(a, y2, label="x squared to 1.5", color="green")
# plt.legend() # call legend to display labels
# plt.title("Multiple line with legend")
# plt.show()


# shows mulitiple charts in one figure
# syntax: plt.subport(rows, cols, index) split figure into grid, index -> which subport you're plotting

# plt.figure(figsize=(8, 4)) # create figure and size 8w and 4h
# plt.subplot(1, 2, 1) # draw multiple plot in one figure means one row, 2 colums, and first plot at left
# plt.plot(a, y1, color="blue", marker="o")
# plt.title("X squared")

# second subport
# plt.subplot(1, 2, 2) # place the second plot to the right 
# plt.plot(a, y2, color="green", linestyle="--")
# plt.title("x^1.5")

# plt.tight_layout() # adjust spaces between plots to avoid overlap
# plt.show()
