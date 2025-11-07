"""
4. Find the Maximum Element
Given a list of numbers, find the maximum element using reduce.
Example:
	numbers = [10, 3, 25, 7, 18]
"""
from functools import reduce

numbers = [10, 3, 25, 7, 18]
max_num = reduce(lambda x, y: x if x > y else y, numbers)

print("Biggest number: ")
print(max_num)