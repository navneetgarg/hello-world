# https://www.youtube.com/watch?v=MPiz50TsyF0&list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_&index=3

from matplotlib import pyplot as plt

# print(plt.style.available)
# plt.style.use("fivethirtyeight")  # - big text
plt.style.use("ggplot")  # - shaded grid
# plt.xkcd()  # non-informal style - funny

# slices = [20, 60, 30, 10]
# labels = ["20", "Sixty", "thirty", "ten"]

labels = [
    "JavaScript",
    "HTML/CSS",
    "SQL",
    "Python",
    "Java",
]
slices = [
    59218,
    55465,
    47544,
    36442,
    35916,
]

explode = [0, 0, 0, 0.1, 0]
# explode the python: 10% of the radius


# colors = [
#     "#008fd5",
#     "#fc4f30",
#     "#e5ae37",
#     "#6d904f",
# ]

# plt.pie(slices, labels=labels, colors=colors, wedgeprops={"edgecolor": "black"})
# wedgeprops for the line at the edges of each pie-portion

plt.pie(
    slices,
    labels=labels,
    explode=explode,
    shadow=True,
    startangle=90,  # first item starts with 90 deg angle
    autopct="%1.1f",  # format string to denote the percent in pie-portions
    wedgeprops={"edgecolor": "black"},
)
# pie chart dont look good with large data

plt.title("My awesome pie chart")


plt.tight_layout()
plt.show()


# multiple lines copy with alt-select -> ctrl+c -> select to replace(cursor should be at starting point) -> ctrl+v

# colors:
# Blue: #008fd5
# Red: #fc4f30
# Yellow: #e5ae37
# Green: #6d904f
