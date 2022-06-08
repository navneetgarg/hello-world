# https://www.youtube.com/watch?v=nKxLfUrkLE8&list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_&index=2

# from cProfile import label
from collections import Counter

# import csv
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# print(plt.style.available)
# plt.style.use("fivethirtyeight") #- big text
plt.style.use("ggplot")  # - shaded grid
# plt.xkcd()  # non-informal style - funny


data = pd.read_csv("data.csv")
ids = data["Responder_id"]
lang_responses = data["LanguagesWorkedWith"]

# print(row["LanguagesWorkedWith"].split(";"))
lang_counter = Counter()
for response in lang_responses:
    lang_counter.update(response.split(";"))

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
plt.show()
