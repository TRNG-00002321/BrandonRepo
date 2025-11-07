"""
3. Concatenate Strings
Given a list of strings, concatenate them into a single string using reduce.
Example :
	words = ["Python", "is", "awesome", "!"]
"""

from functools import reduce

words = ["Python", "is", "awesome", "!"]

string = reduce(lambda x, y: x + " "+ y, words)

print("Your string is:")
print(string)