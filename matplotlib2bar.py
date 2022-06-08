# https://www.youtube.com/watch?v=nKxLfUrkLE8&list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_&index=2

from cProfile import label
from matplotlib import pyplot as plt
import numpy as np

# first plot=======================================================
# print(plt.style.available)
# plt.style.use("fivethirtyeight") #- big text
plt.style.use("ggplot")  # - shaded grid
# plt.xkcd()  # non-informal style - funny

# x-axis
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
x_indices = np.arange(len(dev_x))
width = 0.25

# y-axis
dev_y = [3800, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

# format string: fmt = [marker][line][color]; like in MATLAB

plt.bar(x_indices, dev_y, label="plot1", width=width)  # okay
# color hex like '#444444' can be used; 2 letters for R, G & B.

# overlapping if we plot others; for side by side: we do numpy x_indices
plt.bar(x_indices - width, dev_y, label="plot2", width=width)  # okay

# plt.legend(["plot 1", "plot 2"])
plt.xticks(ticks=x_indices, labels=dev_x)
plt.title("Median salay (USD) by Age")
plt.ylabel("Salary")
plt.xlabel("Age")
plt.legend()
# plt.grid(True)

plt.tight_layout()

plt.savefig("matplotlib2.png")
plt.show()
