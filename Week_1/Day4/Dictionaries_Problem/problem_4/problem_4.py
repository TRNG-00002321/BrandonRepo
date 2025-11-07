"""
4. Write a Python program to add a key to a dictionary
Sample Output
dictionary = {"Name" : "Ram" , "Age" : 23}
add_key = {"City" : "Salem"}
dictionary = {'Name' : 'Ram', 'Age' : 23, 'City' : 'Salem'}

"""

dictionary = {"Name" : "Ram" , "Age" : 23}
extra_key = {"City" : "Salem"}


def add_key_func(dict, key):
    dict.update(key)
    print(dict)

add_key_func(dictionary, extra_key)