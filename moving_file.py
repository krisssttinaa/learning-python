import os

source = "/Users/krisss/Documents/temp.txt"
destination = "/Users/krisss/Desktop/temp.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")