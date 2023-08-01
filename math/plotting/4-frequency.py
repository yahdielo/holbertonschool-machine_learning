#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

plt.hist(student_grades, bins=range(0, 101, 10), edgecolor='black')
plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.title("Project A")
plt.margins(x=0)
plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
plt.yticks([0, 5, 10, 15, 20, 25, 30])
plt.ylim(0)
plt.xlim(0)
plt.show()
