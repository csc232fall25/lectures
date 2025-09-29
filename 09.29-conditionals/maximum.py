x = int(input("What is an integer? "))
y = int(input("What is another integer? "))
z = int(input("What is another integer? "))

if x > y:
    # NOTE: By themselves, a pair of nested "if..."s is essentially equivalent to
    #       an "if...and...".
    if x > z:
        print("The maximum is " + str(x) + ".")
    else:
        print("The maximum is " + str(z) + ".")
else:
    # NOTE: But by splitting an "if...and..." into two nested "if..."s, we can
    #       attach a different "else..." to each "if...".
    if y > z:
        print("The maximum is " + str(y) + ".")
    else:
        print("The maximum is " + str(z) + ".")
