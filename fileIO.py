import os
import time



fPath = os.path.join('C:\\Users\\green\\OneDrive\\Desktop\\test')

fTime = os.path.getmtime(fPath)
fLocalTime = time.ctime(fTime)


for file in os.listdir(fPath):
    if file.endswith(".txt"):
        fName = os.path.join(fPath, file)
        print("\n{} \nlast edited {}\n".format(fName, fLocalTime))

