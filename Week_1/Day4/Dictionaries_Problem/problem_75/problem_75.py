"""
75. Write a Python program to iterate over dictionaries using for loops.
Sample Output
{"Name" : "Ram" , "Age" : 23 , "City" : "Salem", "Gender" : "Male"}
Name : Ram
Age : 23
City : Salem
Gender : Male

"""

my_dict = {"Name" : "Ram" , "Age" : 23 , "City" : "Salem", "Gender" : "Male"}

for key,value in my_dict.items():
    print(f"{key} : {value}")