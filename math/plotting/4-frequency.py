#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

fig, ax = plt.subplots()
bar_width = 1
y = np.arange(0, len(student_grades))

plt.hist(student_grades, bins=range(0, 101, 10), edgecolor='black')
plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.show()
