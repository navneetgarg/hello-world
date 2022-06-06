# main.py

# print "add"
a = 2
print(a)

import json

items = json.loads('[{"id":1,"text": "Item 1"},{"id":2,"text": "Item 2"}]')

for item in items:
    print(item["text"])


def addd(x, y):
    return x + y


def test_addd():
    assert addd(2, 1) == 3


test_addd()

a = a + 1
print(a)

# New python environment and activation
# python -m venv venv
# venv\Scripts\activate.bat

# AREPL - evaluate as "you type"/make changes
# Kite - autocomplete plugin
# autodoc - for documentation of functions
# pytest enable in settings, and install by pip
# https://www.youtube.com/watch?v=-nh9rCzPJ20 settings json edit

# file-con theme ayu
