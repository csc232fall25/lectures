# NOTE: Here, i is the "loop counter"; it counts how many times the loop has
#       "iterated" and determines when the loop should stop repeating (when
#       we should "break out" of the loop).
i = 0
while i < 10:
    print("The value of i is " + str(i) + ".")
    i = i + 1

# NOTE: If the condition is never true, the loop will never run at all...
i = 0
while i > 10:
    print("The value of i is " + str(i) + ".")
    i = i + 1

# NOTE: ...if the condition is never false, the loop runs infinitely.
# i = 0
# while i > -1:
#     print("The value of i is " + str(i) + ".")
#     i = i + 1

# NOTE: Alternatively, the above "while" is equivalent to the below "for".
#       Essentially, a "for" loop allows the interpreter to generate the
#       possible values of i for us, so that there is less danger of
#       inadvertently generating infinitely many values of i.
for i in range(10):
    print("The value of i is " + str(i) + ".")

# NOTE: If "range" is given three values instead of one, the first is where
#       to start, the second is where to stop, and the third is the
#       difference between each value of i.
for i in range(9, -1, -1):
    print("The value of i is " + str(i) + ".")

# NOTE: By convention, the loop counter is typically named "i", but there is
#       nothing special about "i". In particular, if we nest a second loop
#       within, we cannot use "i" a second time.
for i in range(2):
    for j in range(3):
        print("The values of i and j are " + str(i) + ", " + str(j) + ".")

# NOTE: The nested loops below result in the same six combinations of i and j
#       as those above, but in a different order.
for j in range(3):
    for i in range(2):
        print("The values of i and j are " + str(i) + ", " + str(j) + ".")