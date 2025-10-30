# NOTE: An array is more limited than a list, but those limitations mean that
#       an array can potentially be more efficient than a list. However, Python
#       doesn't have true arrays, so we need the assistance of the third-party
#       library NumPy:
import numpy as np
import sys

# NOTE: NumPy arrays have two key limitations: their size is fixed, and every
#       element must have the same type. Otherwise, they behave much like
#       Python lists, except that they are stored in a more efficient way
#       behind the scenes.
array = np.array([1, 2, 3, 4])
print(array)
print(array[2])
print(array[-1])
print(array[1:3])
print(array[-2:])
print(array[4])

# NOTE: NumPy was designed for scientific and mathematical computations, where
#       it makes more sense to operate on the individual elements of arrays,
#       rather than on the arrays as a whole:
print(array * 2)
print(array + 1)
print(array + np.array([1, 2, 3, 4]))
print(np.concatenate((array, np.array([1, 2, 3, 4]))))
print(array == 1)
print(array == np.array([1, 2, 3, 4]))
print(np.array_equal(array, np.array([1, 2, 3, 4])))

# NOTE: The shape of a NumPy array is its dimensions; operations such as
#       concatentation only make sense when the shapes align. Here, given a
#       2x2 and a 2x1, it makes sense to place the 2x1 to the right of the 2x2,
#       but not below the 2x2.
print(array.shape)
matrix = np.array([[1, 2], [3, 4]])
print(matrix)
print(matrix.shape)
column = np.array([[5], [6]])
print(column)
print(column.shape)
print(np.concatenate((matrix, column), axis = 1))
print(np.concatenate((matrix, column), axis = 0))

# NOTE: To make a very long story short, NumPy not only makes use of true
#       arrays, which are faster than ordinary lists, but it also implements
#       common operations such as matrix multiplication behind the scenes in
#       more efficient programming languages, such as C or Fortran. This allows
#       us to access the power of a language like C within our existing Python
#       programs.
n = int(sys.argv[1])
matrix_a = np.random.randint(0, 10, (n, n))
matrix_b = np.random.randint(0, 10, (n, n))
matrix_c = np.matmul(matrix_a, matrix_b)
