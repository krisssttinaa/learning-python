#check if file exists on some place in our computer
import os
path= "/Users/krisss/Desktop/temp.txt"
if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That location doesn't exists")