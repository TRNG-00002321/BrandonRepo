"""
3. Add Corresponding Elements: Given two lists of numbers of the same length, use map() to
return a new list containing the sum of corresponding elements.
Example
	list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    # Expected output: [5, 7, 9]
"""

def find_sum():
    pass

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list_obj = map(lambda x, y: x + y, list1, list2)
list3 = list(list_obj)
print(list3)