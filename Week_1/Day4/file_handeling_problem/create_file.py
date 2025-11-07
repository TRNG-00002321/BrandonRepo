# creating a new file use "x" mode to create a new file
# if the file already exists, it raises a fileexistserror

try:
    with open("newfile.txt", "x") as file:
        file.write("This is a new file.")
except FileExistsError:
    print("File already exists")
