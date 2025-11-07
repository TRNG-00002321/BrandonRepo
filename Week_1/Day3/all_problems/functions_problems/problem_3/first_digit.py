"""
3. Given a number n, find the first digit of the number.

"""
def first_digit(n):
    return(str(n)[0])

number = int(input("Enter a big number: "))
first_digit = first_digit(number)

print(f"the first digit is: {first_digit}")