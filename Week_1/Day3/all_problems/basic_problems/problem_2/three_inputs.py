"""
2. Given three inputs that are stored in the variables a, b, and c.
You need to print a, a times and b, b times  in a single line separated by c.

"""

value_a = int(input("enter value of a: "))
value_b = int(input("enter value of b: "))
value_c = (input("enter value of c: "))

def load_values(value):
    string = ""
    for _ in range(value):
        string += str(value)
    return string

str1 = load_values(value_a)
str2 = load_values(value_b)

print(str1+value_c+str2)

