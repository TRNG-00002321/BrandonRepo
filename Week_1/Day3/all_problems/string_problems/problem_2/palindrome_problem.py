"""
2. Given a string s, you need to check if it is palindrome or not.
A palindrome is a string that reads the same from front and back.
"""

s = input("Enter a string: ")
s2 = s[::-1]

print(f"Your string is now: {s2}")

if s2 == s:
    print("String IS a palindrome")
else:
    print("string is NOT palindrome")