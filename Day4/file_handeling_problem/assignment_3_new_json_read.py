#read the information specifically based on the user only.
#do not read the other information on any other user/identity

import json

with open("data.json", "r") as f:
    data = json.load(f)

person = next((x for x in data if x["name"] == "Brandon"), None)

if person:
    print(person)
else:
    print("Person not found")
