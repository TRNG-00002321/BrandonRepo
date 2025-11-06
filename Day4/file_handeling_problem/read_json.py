import json

# open the JSON file in read mode ('r')
with open("data.json", "r") as f:
    # load the JSON data from the file into a python dictionary
    data = json.load(f)

#now, 'data' is a python dictionary containing the information from data.json
print(data)