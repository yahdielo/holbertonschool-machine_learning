#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))
fruits = ['Apples', 'Bananas', 'Oranges', 'Peaches']
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']
x = [ "Farra", "Fred", "Felicia"]

apples = fruit[0]
bananas = fruit[1]
oranges = fruit[2]
peaches = fruit[3]



plt.bar(x, apples, color=colors[0], width=0.5, label=fruits[0])
plt.bar(x, bananas, bottom=apples, color=colors[1], width=0.5, label=fruits[1])
plt.bar(x, oranges, bottom=apples + bananas, color=colors[2], width=0.5, label=fruits[2])

# Set y-axis limits and ticks
plt.ylim(0, 80)
plt.yticks(np.arange(0, 81, 10))
# titles
plt.title("Number of Fruit per Person")
plt.legend(fruits, loc="upper right")
plt.ylabel("Quantity of Fruit")
plt.legend()
plt.show()