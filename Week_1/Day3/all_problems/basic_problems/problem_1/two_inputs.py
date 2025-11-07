"""
1. Given two inputs that are stored in variables a and n,
you need to print a, n times in a single line without space between them.
Output must have a newline at the end.
"""

a = int(input("first value: "))
n = int(input("second value: "))

def printer(a, n):
    for i in range(n):
        print(a, end='')
    print()

printer(str(a), n)