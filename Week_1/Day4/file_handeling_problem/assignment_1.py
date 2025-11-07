#read a file and copy that content into a new file

file = open("example_text.txt","r")
content = file.read()

with open("example_text2.txt", "w") as file:
    file.write(content)
file.close()