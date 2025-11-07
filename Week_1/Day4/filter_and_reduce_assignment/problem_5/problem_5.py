"""
5. Flatten a List of Lists
Given a list of lists, flatten it into a single list using reduce.
Example:
	list_of_lists = [[1, 2], [3, 4], [5, 6]]
"""
from functools import reduce

list_of_lists = [[1, 2], [3, 4], [5, 6]]
new_list = reduce(lambda acc, y: acc + y, list_of_lists, [])
print("new list: ")
print(new_list)