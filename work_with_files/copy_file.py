# copyfile() = copies contents of a file
# copy() =     copyfile() +permission mode +destination can be a directory
# copy2()=     copy() +copies metadata (file's creation and modification times)

import shutil

shutil.copyfile("/Users/krisss/Desktop/temp.txt", "/Users/krisss/Desktop/test.txt")
#shutil.copy("/Users/krisss/Desktop/temp.txt", "/Users/krisss/Desktop/test.txt")
#shutil.copy2("/Users/krisss/Desktop/temp.txt", "/Users/krisss/Desktop/test.txt")