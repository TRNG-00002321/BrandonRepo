"""
3. You are given a list arr that contains integers. You need to return average of the non negative integers.
Examples:
Input: arr = [-12, 8, -7, 6, 12, -9, 14]
Output: avg = 10.0
Explanation: The non negative numbers are 8 6 12 14. The sum is 8+6+12+14 = 40, Average = 40/4 = 10.0

"""

arr = [-12, 8, -7, 6, 12, -9, 14]

amnt = 0
num_sum = 0

for _ in arr:
    if _ > 0:
        amnt+=1
        num_sum += _

avg = num_sum/amnt

print(avg)