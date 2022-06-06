import math
import sys
import os


import requests

r = requests.get("https://coreyms.com")
# go to definition: F12
print(r.status_code)
# format the code : shft alt F


# linitng: to avoid mistakes
print(sys.version)


def fun(one):
    t = 2
    return one


print(fun(2))

