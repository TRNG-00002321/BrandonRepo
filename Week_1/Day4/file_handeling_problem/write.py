# writing to a file : use "w" mode to write to a file
# if the file exists, it will be overwritten

with open("output.txt", "w") as file:
    file.write("This is a test.\n")
    file.write("This is a test part 2!.\n")