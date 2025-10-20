# NOTE: A list is essentially a string whose elements need not be characters.
#       Like strings, lists are indexed collections of multiple values.
print([1] + [2, 3])
print([1, 2, 3] == [1, 2, 3])
print([1, 2, 3] == [3, 2, 1])

# NOTE: Unlike strings, the elements of a list may have any type. Here, they
#       are integers; they don't have to be characters.
print("1" in [1, 2, 3])
print(1 in [1, 2, 3])

# NOTE: Lists and be indexed and sliced just like strings...
lst = [5, "csc232", 3.14]
lst = lst + [False]
print(lst[2])
print(lst[-1])
print(lst[1:3])
print(lst[-2:])
# print(lst[4])

# NOTE: Unlike all of the functions that operate on strings, the functions that
#       operate on lists typically modify the list in-place. Here, the append
#       function doesn't return a new list; rather, after it returns, the old
#       list now contains the appended element.
lst = [2, 1, 13, 3, 1, 5, 0]
print(lst)
print(lst.append(8))
print(lst)
print(lst.reverse())
print(lst)

# NOTE: That is, the default, common sense behavior is to avoid making a copy.
#       If we the programmers happen to know that we need to preserve the
#       original list, then Python provides a function to make a copy of that
#       list first.
lst2 = lst.copy()
lst2.sort()
print(lst2)
print(lst)

# NOTE: Alternatively, rather than explicity typing out the elements of a list,
#       a list comprehension describes how to compute each element of the list.
print([x for x in range(10)])
print([x * 2 for x in range(10)])
print([x * 2 for x in range(0)])
print([x for x in range(10) if x % 2 == 0])
print([x * 2 for x in range(10) if x % 2 == 0])

# NOTE: It is, as it turns out, possible to conditionally operate on some
#       elements and not on others, while still including all elements...
print([x * 2 if x % 2 == 0 else x for x in range(10)])

# NOTE: ...however, for more complex computations like this, a list
#       comprehension is equivalent to a loop, and a loop is both easier
#       to read and easier to modify in the future.
lst = []
for x in range(10):
    if x % 2 == 0:
        lst.append(x * 2)
    else:
        lst.append(x)
print(lst)