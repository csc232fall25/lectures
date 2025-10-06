# NOTE: This function takes no arguments and returns a value.
def get_leg():
    return int(input("How long is one leg? "))

# NOTE: This function takes two arguments and returns a value.
def hypotenuse(a, b):
    return (a ** 2 + b ** 2) ** 0.5

# NOTE: Without functions, these two lines would be practically identical. We
#       have to write the same code twice, and if we ever want to change that
#       code in the future, we have to remember to make the same change twice.
side_a = get_leg() 
side_b = get_leg() 

# NOTE: Without functions, this line would arguably be somewhat cryptic. It
#       may not be immediately obvious at a glance, especially if we were to
#       come back later and try to read it, what it is trying to do.
side_c = hypotenuse(side_a, side_b)
print("The hypotenuse has length " + str(side_c))
