"""
2. Capitalize a List of Names: Given a list of names, use map() to
return a new list where each name is capitalized.
Example
    names = ["alice", "bob", "charlie"]
    # Expected output: ["Alice", "Bob", "Charlie"]
"""

def cap_name(name):
    return(name.capitalize())

names = ["alice", "bob", "charlie"]

capitalized_names_object = map(cap_name, names)

capitalized_names = list(capitalized_names_object)
print(capitalized_names)