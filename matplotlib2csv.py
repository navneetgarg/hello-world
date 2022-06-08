# https://www.youtube.com/watch?v=nKxLfUrkLE8&list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_&index=2

# from cProfile import label
from collections import Counter
import csv
from matplotlib import pyplot as plt
import numpy as np

# print(plt.style.available)
# plt.style.use("fivethirtyeight") #- big text
plt.style.use("ggplot")  # - shaded grid
# plt.xkcd()  # non-informal style - funny

# counter list
c = Counter(["Python", "Java"])
print(c)
c.update(["Python", "C++"])
print(c)

with open("data.csv") as csvfile:
    csvreader = csv.DictReader(csvfile)
    row = next(csvreader)
    # print(row["LanguagesWorkedWith"].split(";"))
    lang_counter = Counter()
    for row in csvreader:
        lang_counter.update(row["LanguagesWorkedWith"].split(";"))

print(lang_counter.most_common(15))

# separate languages and popularities
langs = []
pops = []
for item in lang_counter.most_common(15):
    langs.append(item[0])
    pops.append(item[1])
print(langs)
print(pops)


# plot lang vs pop
# plt.bar(langs, pops)

langs.reverse()
pops.reverse()
plt.barh(langs, pops)  # barh for horizontal chart
plt.title("Most popular languages")
plt.xlabel("Number of peoples who use")

plt.tight_layout()
# plt.show()
