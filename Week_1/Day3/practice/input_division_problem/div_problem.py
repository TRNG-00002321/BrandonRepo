a = input("Enter your first number: ")
b = input("Enter your second number: ")


try:

    a = int(a)
    b = int(b)
    print(f"{a} / {b} = {a / b}")

except ZeroDivisionError:
    print("Division by zero.")

except ValueError:
    print("Invalid input. Please enter integers only.")



