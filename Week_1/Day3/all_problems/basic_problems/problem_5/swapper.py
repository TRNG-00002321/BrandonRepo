"""
5. Given two numbers a and b, you need to swap their values so a holds the value of b and b holds the value of a.
Just write the code to swap values of a and b at the specified place.
"""

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = 0

print(f"before swap: a = {a}, b = {b}")

c=a
a=b
b=c

print(f"after swap: a = {a}, b = {b}")