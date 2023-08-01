#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

font_size = 'x-small'

fig, axs = plt.subplots(3, 2)


axs[0, 0].plot(y0, color='red')


axs[0, 1].scatter(x1, y1, color='magenta', s=5)
axs[0, 1].set_title("Men's Height vs Weight", fontsize=font_size)
axs[0, 1].set_xlabel("Height (in)", fontsize=font_size)
axs[0, 1].set_ylabel("Weight (lbs)", fontsize=font_size)

axs[1, 0].plot(x2, y2)
axs[1, 0].set_title("Exponential Decay of C-14", fontsize=font_size)
axs[1, 0].set_xlabel("Time (years)", fontsize=font_size)
axs[1, 0].set_ylabel("Fraction Remaining", fontsize=font_size)

axs[1, 1].plot(x3, y31, c="red", linestyle='dashed')
axs[1, 1].plot(x3, y32, c="green")
axs[1, 1].set_title("Exponential Decay of Radiactive Elements", fontsize=font_size)
axs[1, 1].set_xlabel("Time (years)", fontsize=font_size)
axs[1, 1].set_ylabel("Fraction remaining", fontsize=font_size)

# Remove the empty subplot (axis[2, 0]) to be able to display the chart in the full row
axs[2, 1].axis('off')


axs[2, 0].hist(student_grades, bins=range(0, 101, 10), edgecolor='black')
axs[2, 0].set_title("Project A", fontsize=font_size)
axs[2, 0].set_xlabel("Grades", fontsize=font_size)
axs[2, 0].set_ylabel("Number of Students", fontsize=font_size)

plt.margins(x=0)
plt.margins(x=0)
plt.ylim(0)
plt.xlim(0)

# Adjust the layout to prevent overlapping of titles
plt.tight_layout()

plt.show()