# NOTE: A module is any file containing Python code, and it is possible to
#       import one module into another, such that code written in one file
#       is accessible within another.
import functions

def main():
    print("The value of f(1) is " + str(functions.f(1)) + ".")

# NOTE: The entry point (the point at which execution begins) is the beginning
#       of the module run from the command line. By convention, code for the
#       entry point is typically placed in a function named "main", and the
#       first thing that happens when the program is run is to call main.
if __name__ == "__main__":
    main()