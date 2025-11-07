"""
5. Write a Python program to concatenate following dictionaries to create a new one.
Sample Output
Dictionary 1 = {"Name" : "Ram" , "Age" : 23}
Dictionary 2 = {"City" : "Salem", "Gender" : "Male"}
Concatenate Dictionaries = {'Name' : 'Ram', 'Age' : 23, 'City' : 'Salem', 'Gender': 'Male'}
"""

dictionary1 = {"Name" : "Ram" , "Age" : 23}
dictionary2 = {"City" : "Salem", "Gender" : "Male"}
new_dict={}

new_dict={**dictionary1,**dictionary2}
print(new_dict)