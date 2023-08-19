"""
Open a page with random artstyle
"""

import random
import os


def get_random(num):
    return random.randint(0, num)


with open("styles_list.txt", "r") as file:
    content = file.readlines()
    index = get_random(len(content))
    line = content[index]
    print(index)

url = f'https://www.midlibrary.io/styles/{line}'
print(url)

try:
    os.system("start " + str(url))
except Exception as ex:
    print(ex)


