# sin and cos 
# np.sin() is function used to caliculate sin of angles
# np.cos() is also function used to caliculate cos of angles
# usercase: periodic data like tapmerature over days, sound waves, ..
# simulating motion and rotation in advanced ML like robotics and computer vision , games help model rotation, movement, ..

import numpy as np
# import matplotlib.pyplot as plt

# # create 100 angles start from 0 and to 2pi 
# angles = np.linspace(0, 2 * np.pi, 100)

# # caliculate sin of every angle
# sin_values = np.sin(angles)
# # caliculate cosine of every angle
# cosine_values = np.cos(angles)

# plt.plot(angles, sin_values, label='Sine', color='blue')
# plt.plot(angles, cosine_values, label="Cosine", color='Orange')
# plt.xlabel('Angle (radians)')
# plt.ylabel('Value')
# plt.title("Sine and cosine values")
# plt.legend()
# plt.show()


# this model help ML to understand seasons, time of the day,  weekly patterns
day = 100
day_of_year = 356

sin_day = np.sin(2 * np.pi * day / day_of_year)
cos_day = np.cos(2 * np.pi * day / day_of_year)
print(cos_day, sin_day)