import json

my_data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "isS_student": False,
    "courses": ["Math", "Science"]
}

# open a file in write mode ('w'). if the file doesn't exist, it will be created.
# if it exists, its contents will be overwritten.
with open("data.json", "w") as f:
    # dump the python data into the file in JSON format
    json.dump(my_data, f, indent=4) #'indent=4' makes the output human-readable