import sys

# NOTE: A file is a collection of data that is stored on some non-volatile file
#       system. The contents of a file persist even after a program terminates
#       or the computer restarts; we can access them later via its filename.
with open("test.txt", "r") as test_file:
    string = test_file.read()
    print(string)

with open("test.txt", "r") as test_file:
    lines = test_file.readlines()
    print(lines)

# NOTE: When a file is first opened, the interpreter positions us a the start
#       of that file. Each read or write then advances that position, such that
#       later reads will read data that has not already been read before.
with open("test.txt", "r") as test_file:
    print(test_file.readline())
    print(test_file.readline())
    print(test_file.readline())

with open("test.txt", "r") as test_file:
    for line in test_file:
        print("The next line is " + line)

# NOTE: By convention, the names of files to be read or written are typically
#       passed as command line arguments. These are strings are typed by the
#       user when they first start the program, and they can be accessed within
#       the built-in list sys.argv:
print(sys.argv)

# NOTE: Often, data is stored in tabular form in CSV files, in which each row
#       is a line in the file, and the cells in a row are separated by commas.
#       We can then read that data back into the memory of a running program
#       one line at a time, splitting each line up by commas in order to
#       reconstruct the tabular format.
table = []
with open(sys.argv[1], "r") as test_file:
    for line in test_file:
        row = line.split(",")
        table.append(row)

print(table[5][2])
