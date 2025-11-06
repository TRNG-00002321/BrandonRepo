import sys

#take int from user, match int to option
print("Options: ")
print("1. Water")
print("2. Cola")
print("3. Gatorade")

def handle_transaction(dollar_amount):
    print("Dollar amount: $%.2f" % dollar_amount)

    total_change = 0

    while (total_change < dollar_amount):
        #enter number of quarters
        quarters_amnt = int(input("Enter quarters: "))
        quarters = (.25 * quarters_amnt)

        #enter number of dimes
        dimes_amnt = int(input("Enter dimes: "))
        dimes = (.10 * dimes_amnt)

        #enter number of nickles
        nickles_amnt = int(input("Enter nickles: "))
        nickles = (.05 * nickles_amnt)

        #enter number of pennies
        pennies_amnt = int(input("Enter pennies: "))
        pennies = (.01 * pennies_amnt)

        total_change = (quarters + dimes + nickles + pennies)
        print("Total change given: $%.2f" % total_change)

        if(total_change < dollar_amount):
            print("Not enough. Please try again.")

    print("Change received: Dispensing item")
    change_back(dollar_amount, total_change)


def change_back(dollar_amount, total_change):
    change = total_change - dollar_amount
    print("Your change back: $%.2f" % change)


try:
    choice = int(input("Enter your order: "))
except ValueError:
    print("Invalid input\nExiting...")
    sys.exit()

if choice == 1:
    dollar_amount = float(1)
elif choice == 2:
    dollar_amount = float(2)
elif choice == 3:
    dollar_amount = float(3)
else:
    print("Invalid option")
    sys.exit()

handle_transaction(dollar_amount)