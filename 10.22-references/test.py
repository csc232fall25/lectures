def maximum(lst):
    """
    Find the largest element in a list.

    :param lst: A non-empty list of integers
    :return: The largest integer in the list
    """
    temp = lst[0]

    # NOTE: This is not the only way to write this function -- in fact, there's
    #       a built-in function that already does this for us -- but it does
    #       illustrate the general pattern for working with lists. We first
    #       define a temporary variable (in this case, the first element of the
    #       list), then we iterate over the elements of the list, updating the
    #       temporary variable as necessary to construct a solution to the
    #       problem (in this case, the largest element seen thus far).

    for element in lst:
        if element > temp:
            temp = element
    
    return temp


def scale(lst, scalar):
    """
    Multiply every element of a list by a scalar.

    :param lst: A list of integers
    :param scalar: An integer scalar
    :return: A new list of the scaled elements
    """

    # NOTE: This doesn't work. It modifies the local variable element, which
    #       contains an element from the list, but it doesn't modify the
    #       element in the list itself.
    # for element in lst:
    #     element = element * scalar

    # NOTE: To actually modify an element in a list, we have to know its index.
    #       Note that this modification will be visible outside the function.
    #       This list is not a separate list; it's just a reference to the same
    #       list that was created before calling this function.
    # for i in range(len(lst)):
    #     lst[i] = lst[i] * scalar

    # NOTE: If this is not the desired behavior, the burden is on us as the
    #       programmers to create and return a copy of the list instead.
    temp = []

    for element in lst:
        temp.append(element * scalar)

    return temp


lst = [1, 4, 2, 3]
print(maximum(lst))
print(scale(lst, 2))
print(lst)

# NOTE: The elements in a list may have any type -- they could even be more
#       lists. Here, the 0'th element of matrix is itself a list, which
#       must be indexed again in order to access the integers within.
matrix = [[1, 2, 3, 4], [5, 6, 7]]
print(matrix[0])
print(matrix[0][1])

# NOTE: To add two lists is to concatenate them together, thus, to multiply
#       a list by a scalar is to repeatedly concatenate it to itself.
print(scale(matrix, 2))

# NOTE: There is no requirement that the "inner" lists have the same length,
#       nor that each element of the "outer" list even be an "inner" list. 
# matrix.append(8)
matrix[1].append(8)
print(matrix)