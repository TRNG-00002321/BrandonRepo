"""
6. Write a Python program to check whether a given key already exists in a dictionary.
Sample Output
{'Name' : 'Ram', 'Age' : 23,}
Key = Name
Key is Available in the Dictionary

"""

my_dict = {'Name' : 'Ram', 'Age' : 23, }

#this key already exists in dict
key = "Name"

if key in my_dict:
    #key exists inside the dict
    print(f"Key is Available in the Dictionary")
else:
    #key does not exist in the dict
    print(f"Key is *NOT* Available in the Dictionary")