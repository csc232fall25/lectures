# NOTE: A dictionary is essentially a list whose indices need not be
#       sequential integers:
dct = {"a": "alpha", "b": "beta"}
print(dct["a"])

# NOTE: Since the indices can be almost anything, there is no sense of order
#       to a dictionary. It is possible to index a dictionary just like a
#       string or a list, but it is not possible to slice a dictionary.
dct["c"] = "gamma"
print(dct)

# NOTE: If we want to talk about the "first" element in a dictionary, then we
#       have to convert, for example, its keys into a list first. Lists are
#       indexed, so it then makes sense to talk about the "first" element.
keys = list(dct.keys())
values = list(dct.values())
print(keys)
print(values)
print(keys[1])

# NOTE: Just as with lists, dictionaries can be arbitrarily long. Copying a
#       dictionary takes an arbitrary amount of time, so the interpreter tries
#       to modify existing dictionaries rather than copying them if possible.
other = {"d": "delta", "e": "epsilon"}
dct.update(other)
print(dct)

# NOTE: The keys can still be integers, if desired, but they do not have to be
#       assigned sequentially from 0.
print({x: x ** 2 for x in range(5)})
print({x: x ** 2 for x in range(5) if x % 2 == 1})

# NOTE: It is possible for multiple keys to map to the same value, however, it
#       makes no sense for one key to map to multiple values. If a key is ever
#       reused, remapping a key overwrites its existing value.
print({x: 94 for x in range(5)})
print({94: x for x in range(5)})

# NOTE: Dictionaries contain both keys and values. Between those two, the keys
#       are the more useful piece of information, since knowing a key allows
#       us to look up the corresponding value...
for key in dct:
    print("The key " + str(key) + " maps to the value " + str(dct[key]) + ".")

# NOTE: ...if we the programmers know that we only need the values, then we can
#       always opt-in to this behavior by asking for the values explicity.
for value in dct.values():
    print("A value is " + str(value) + ".")

# NOTE: A dictionary can do anything a list can, and not vice versa, but just
#       because we can do something does not mean we want to give ourselves the
#       opportunity to do it incorrectly. Here, with a list, the interpreter
#       can warn us right away that we have used the indices incorrectly.
# lst = [1, 2, 4, 8]
# lst["4"] = 16
# print(lst)
dct = {0: 1, 1: 2, 2: 4, 3: 8}
dct["4"] = 16
print(dct)