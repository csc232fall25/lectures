# TODO: Suppose the user types "15". What will the following program print?

def divides(a, b):
    """
    NOTE: Once we understand the behavior of a function, we should document
          its purpose so that we don't have to trace through it again in the
          future -- this is a special comment called a "docstring".

    Determine whether or not a divides b.
    :param a: An integer divisor
    :param b: An integer dividend
    :return: Whether or not b is divisible by a
    """
    return b % a == 0


def factors(number):
    factor = 2
    count = 0

    while number > 1:
        if divides(factor, number):
            print(str(factor))
            number = number // factor
            count = count + 1
        else:
            factor = factor + 1

    return count


def main():
    number = int(input("Number? "))

    if factors(number) == 1:
        print(str(number) + " is prime.")
    else:
        print(str(number) + " is not prime.")


if __name__ == "__main__":
    main()
