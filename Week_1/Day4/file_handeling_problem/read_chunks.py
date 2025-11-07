# reading in chunks : useful for large files:

with open("example.txt", "r") as file:
    while chunk := file.read(1024):  # read 1024 chars
        print(chunk)
