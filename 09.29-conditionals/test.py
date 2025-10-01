print("This executes unconditionally.")

# NOTE: An "if" statement allows code to be skipped when a condition is not
#       met. The indentation allows the interpreter to determine which
#       statements are "guarded" by the conditional.
if 1 > 2:
    print("This only executes when 1 > 2.")

print("This also executes uncondtionally.")

# NOTE: Each "if" statement may optionally be followed by an "else" statement,
#       which is essentially equivalent to a second "if" statement whose
#       condition is the opposite of the first.
if 1 > 2:
    print("This only executes when 1 > 2.")
else:
    print("This only executes when 1 <= 2.")

# NOTE: There may also be zero or more "elif" statements. Note that an
#       "if...elif" statement is not necessarily equivalent to two "if"
#       statements, since the conditions may not be mutually exclusive.
if 1 > 2:
    print("This only executes when 1 > 2.")
elif 1 < 2:
    print("This only executes when 1 <= 2 and 1 < 2.")
else:
    print("This only executes when 1 <= 2 and 1 >= 2, i.e., when 1 == 2.")
