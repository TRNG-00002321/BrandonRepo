"""
2. You are given a number k and a list arr[] that contains integers.
You need to return list of numbers that are less than k.

Example
Input: arr[] = [54, 43, 2, 1, 5], k = 6
Output: 2 1 5
Explanation: 2 1 5 are less than 6.

"""

arr = [42, 23, 53, 11, 25, 74, 72, 78, 44, 21, 29, 16, 17, 36, 109, 209]
new_arr = []
#given some number k, return a list less than k
k = int(input("Enter a number: "))

for _ in arr:
    if k > _:
        new_arr.append(_)

print(new_arr)