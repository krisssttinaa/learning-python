import os
import shutil
path = "/Users/krisss/Desktop/temp.txt"

try:
    #os.remove(path)    #delete a file
    #os.rmdir(path)     #delete an empty directory
    shutil.rmtree(path) #delete the directory and all the files in it
except FileNotFoundError:
    print(path+" was NOT found")
except PermissionError:
    print("You do not have permission to delete that")
    #for example you can not delete empty folder
except OSError:
    #because if we are using os.rmdir(path)
    #we can not delete a directory that has elements
    #use shuntil for that
    print("You can not delete that using that function")
else:
    print(path+" was deleted")  