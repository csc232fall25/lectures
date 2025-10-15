# NOTE: Unlike ints, floats, and booleans, strings are collections of 
#       multiple values.
print("h" + "ello")
print("hello" == "helo")
print("e" in "hello")

# NOTE: Essentially, some operations only make sense on strings, so they are
#       defined as functions that are part of the string type itself, and
#       accessed using the dot operator.
print("hello".upper())
print("hello".replace("h", "j"))
print("hello".find("e"))

# NOTE: Each character in a string is associated with a sequential integer
#       index, starting from 0. Note that negative indices work backwards
#       from the end of the string.
string = "abcd"
print(string[2])
# print(string[4])
print(string[-1])
# print(string[-5])

# NOTE: Alternatively, strings can be sliced. A slice is essentially a range
#       of indices from a start (inclusive) to an end (exclusive).
print(string[1:3])
print(string[:3])
print(string[-2:])
print(string[:])

# NOTE: This is the general pattern for iterating over the characters in a
#       string. First, the len function computes the length of the string.
#       Then, the range function is used to generate all valid indices
#       within the string, such that i is not just the loop counter, it also
#       happens to be the index of the next character in the string.
for i in range(len(string)):
    print("The character at index " + str(i) + " is " + string[i] + ".")

# NOTE: Alternatively, strings are also iterables. However, iterating over the
#       string itself rather than its indices means that we don't know which
#       character we're on, we only know what that character is -- we have no
#       way of accessing the character's surrounding context within the string.
for char in string:
    print("The next character is " + char + ".")