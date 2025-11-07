"""
1.Given an array arr[], find the first repeating element. The element should occur
more than once and the index of its first occurrence should be the smallest.
Examples:
Input: arr[] = [1, 5, 3, 4, 3, 5, 6]
Output: 2
Explanation: 5 appears twice and its first appearance is at index 2 which is less
than 3 whose first the occurring index is 3.

"""


#arr = [1, 5, 3, 4, 3, 5, 6]
arr = [1, 2, 3, 4, 9, 2, 7]


#pretty difficult
def first_repeat_el(arr):
    seen = {}
    min_i = len(arr)

    for i, val in enumerate(arr):
        if val in seen:
            if seen[val] < min_i:
                min_i = seen[val]
        else:
            seen[val] = i

    if min_i == len(arr):
        return -1
    else:
        return min_i + 1


print(first_repeat_el(arr))
