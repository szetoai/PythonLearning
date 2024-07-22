'''
"r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
'''
# r - reading mode
# read can input int for # of chars (blank for all)
# with auto closes file after use (no need for file.close())
with open("C:/Users/hazfr/OneDrive/Desktop/Code/PythonLearning/D19REF_read.txt") as txt:
    print(txt.read())
# readline reads only first line
with open("C:/Users/hazfr/OneDrive/Desktop/Code/PythonLearning/D19REF_read.txt") as txt:
    print(txt.readline())
# readlines returns list of lines
with open("C:/Users/hazfr/OneDrive/Desktop/Code/PythonLearning/D19REF_read.txt") as txt:
    print(txt.readlines())
# splitlines also returns list of lines, without the \n at end of lines
with open("C:/Users/hazfr/OneDrive/Desktop/Code/PythonLearning/D19REF_read.txt") as txt:
    print(txt.read().splitlines())

# a - append mode, adds onto end
with open("C:/Users/hazfr/OneDrive/Desktop/Code/PythonLearning/D19REF_append.txt", "a") as app:
    app.write("This got added in!")

# w - write mode, replaces text
with open("C:/Users/hazfr/OneDrive/Desktop/Code/PythonLearning/D19REF_write.txt", "w") as writing:
    writing.write("This overwrote what came before!")

# removing files
import os
if os.path.exists("C:/Users/hazfr/OneDrive/Desktop/Code/PythonLearning/D19REF_write.txt"):
    os.remove("C:/Users/hazfr/OneDrive/Desktop/Code/PythonLearning/D19REF_write.txt")