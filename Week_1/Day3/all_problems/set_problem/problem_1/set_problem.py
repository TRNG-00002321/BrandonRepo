"""
1. You are given an array arr[] of size n.
You have to insert all elements of arr[] into a set and return that set .
You are also given a interger x. If x is found in set then erase it from set and print "erased x",
otherwise, print "not found".

"""
x = int(input("Enter a number: "))
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100]

set = {23, 64, 38, 233}

for _ in arr:
    set.add(_)

if x in set:
    set.remove(x)
    print("erased ", x)
else:
    print(f"{x} not found in list")

print(f"set: {set}")

