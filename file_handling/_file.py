'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist, append to the end of the file
"w" - Write - Opens a file for writing, creates the file if it does not exist, overwrite the entire file
"x" - Create - Creates the specified file, returns an error if the file exists

The file should be handled as binary or text mode:
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
'''

import os, time

f = open('test.txt', 'rt')      # == open('test.txt')
#print(f.read())
#print(f.read(5))               # read the first 5 characters
print(f.readline())             # read the first line
f.close()


f = open('test.txt')
for line in f:
    print(line, end='')
f.close()


f = open('newfile.txt', 'w')
f.write("This is a new line!\n")
f.close()
f = open("newfile.txt", 'a')
f.write("Append a new line!")
f.close()


# remove file
if os.path.exists('newfile.txt'):
    os.remove('newfile.txt')
else: pass