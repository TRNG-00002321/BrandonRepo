# handling file paths : use raw strings or os.path for

import os

path = os.path.join("example.txt") #path would go here if needed
with open(path, "r") as file:
    print(file.read())