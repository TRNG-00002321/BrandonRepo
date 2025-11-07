"""
4. Concatenate Strings: Given two lists of strings, use map() to concatenate
corresponding elements with a space in between.
Example
    first_names = ["John", "Jane"]
    last_names = ["Doe", "Smith"]
    # Expected output: ["John Doe", "Jane Smith"]
"""

first_names = ["John", "Jane"]
last_names = ["Doe", "Smith"]

names_map_obj = map(lambda x, y: x + " " + y, first_names, last_names)
full_name_list = list(names_map_obj)
print(full_name_list)