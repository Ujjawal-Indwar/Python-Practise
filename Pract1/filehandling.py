#open()
#open("myfile.txt",'mode')
#mode: Creating of file, writing, reading or appending
# x: just for file creation in case the file does not exit
# w: opens a file for writing  and overwrites what is already written inside
# r: opens a file for reading. throws error if the file does not already exist
# a: opens a file for appending. Does not overwrites the existing content
# w+: writing at the same time
# r+: opens a file for reading and writing
# a+: opens a file for appending and reading
# remove() to delete a file
import os
try:
   ''' f=open("testfile.txt", "w")
    f.write("This is created")'''
   f=open("testfile.txt","r")
   print(f.read())
except IOError as e:
    print(e)
else:
    print("file successfully created")
finally:
    print("file closed")
    f.close()

os.remove("testfile.txt")