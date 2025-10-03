import numpy as np

student_marks = np.array([45, 50, 55, 65, 70, 75, 80, 85, 90, 95, 100])
print("All marks", student_marks)

above = student_marks[student_marks >= 50]
print("Sutdent above 50%", above)

# top three secores
top = np.sort(student_marks)[-3:][::-1]
# [-3:] -> takes three last elements
# ::-1 reverse an array
print("top 3 ", top)