#write a python script to copy an image

source = "circle.png"
destination = "circle_copy.png"

with open(source, "rb") as src_file:
    data = src_file.read()

with open(destination, "wb") as dst_file:
    dst_file.write(data)

print("file copied successfully")