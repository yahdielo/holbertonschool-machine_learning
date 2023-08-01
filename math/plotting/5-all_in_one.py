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
fid = plt.figure()

axs1 = plt.subplot2grid(shape=(3, 2), loc=(0, 0), colspan=1)
axs2 = plt.subplot2grid(shape=(3, 2), loc=(0, 1), colspan=1)
axs3 = plt.subplot2grid(shape=(3, 2), loc=(1, 0), colspan=1)
axs4 = plt.subplot2grid(shape=(3, 2), loc=(1, 1), colspan=1)
axs5 = plt.subplot2grid(shape=(3, 2), loc=(2, 0), colspan=2)



axs1.plot(y0, color='red')
axs1.margins(x=0)

axs2.scatter(x1, y1, color='magenta', s=5)
axs2.set_title("Men's Height vs Weight", fontsize=font_size)
axs2.set_xlabel("Height (in)", fontsize=font_size)
axs2.set_ylabel("Weight (lbs)", fontsize=font_size)

axs3.plot(x2, y2)
axs3.set_title("Exponential Decay of C-14", fontsize=font_size)
axs3.set_xlabel("Time (years)", fontsize=font_size)
axs3.set_ylabel("Fraction Remaining", fontsize=font_size)
axs3.margins(x=0)


axs4.plot(x3, y31, c="red", linestyle='dashed')
axs4.plot(x3, y32, c="green")
axs4.set_title("Exponential Decay of Radiactive Elements", fontsize=font_size)
axs4.set_xlabel("Time (years)", fontsize=font_size)
axs4.set_ylabel("Fraction remaining", fontsize=font_size)
axs4.margins(x=0)

axs5.hist(student_grades, bins=range(0, 101, 10), edgecolor='black')
axs5.set_title("Project A", fontsize=font_size)
axs5.set_xlabel("Grades", fontsize=font_size)
axs5.set_ylabel("Number of Students", fontsize=font_size)

"""
plt.margins(x=0)
plt.ylim(0)
plt.xlim(0)

"""
plt.tight_layout()
plt.show()