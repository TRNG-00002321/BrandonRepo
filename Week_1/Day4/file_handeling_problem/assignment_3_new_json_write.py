"""
write some data, dict into a file,
from input from the console
"enter your name" take name, etc
city age
read from that json file and search for that data
"""
import json
import os

# receive data from user : name, age, city, etc
name = input("enter your name: ")
age = input("enter your age: ")
city = input("enter your city: ")

# create dictionary with this information
my_dict = {
    "name": name,
    "age": age,
    "city": city
}

if os.path.exists("data.json"):
    with open("data.json", "r") as f:
        data = json.load(f)
else:
    data = []

print(my_dict)
data.append(my_dict)

# write (store) it to json (data.json)
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)