# https://www.youtube.com/watch?v=UO98lJQ3QGI
# https://www.youtube.com/watch?v=UO98lJQ3QGI&list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_

from cProfile import label
from matplotlib import pyplot as plt

# first plot=======================================================
print(plt.style.available)
# plt.style.use("fivethirtyeight") #- big text
# plt.style.use("ggplot") #- shaded grid
plt.xkcd()  # non-informal style - funny

# x-axis
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
# y-axis
dev_y = [3800, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

# format string: fmt = [marker][line][color]; like in MATLAB

plt.plot(dev_x, dev_y, "*-r", label="plot1")  # okay
plt.plot(
    dev_x, dev_y, color="b", linestyle="--", marker="o", label="plot1", linewidth=3
)  # also okay
# color hex like '#444444' can be used; 2 letters for R, G & B.


# plt.legend(["plot 1", "plot 2"])

plt.title("Median salay (USD) by Age")
plt.ylabel("Salary")
plt.xlabel("Age")
plt.legend()
plt.grid(True)

plt.tight_layout()

plt.savefig("matplotlib1.png")
# plt.show()

# second plot BAR====================================================
from matplotlib import pyplot as plt2

plt2.bar(dev_x, dev_y, "*-r", label="plot1")  # okay
plt2.tight_layout()
plt2.show()
