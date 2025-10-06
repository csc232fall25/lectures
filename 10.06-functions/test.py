def f():
    print("In f, x has value " + str(x) + ".")

# NOTE: This x is local: it is defined inside the function f, and it is thus
#       only accessible inside of the function f.
def g():
    x = 2
    print("In g, x has value " + str(x) + ".")

# NOTE: This x also turns out to be local: it is a parameter of the function h,
#       and it is thus only accessible inside of the function h.
def h(x):
    x = 4
    print("In h, x has value " + str(x) + ".")

# NOTE: This x is global: it is defined outside of any function, and it is thus
#       accessible inside of any function.
x = 1
print("Before f, x has value " + str(x) + ".")
f()
print("Between f and g, x has value " + str(x) + ".")
g()
print("Between g and h, x has value " + str(x) + ".")
h(x)
print("After h, x has value " + str(x) + ".")