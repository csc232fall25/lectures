import sys
import random


def randomize(size):
    """
    Create a square matrix of random one-digit integers.

    :param size: A desired dimension of the matrix
    :param return: A random matrix of that dimension
    """
    return [[random.randint(0, 9) for _ in range(size)] for _ in range(size)]


def multiply(matrix_a, matrix_b):
    """
    Mupliply two matrices.

    :param matrix_a: A first square matrix
    :param matrix_b: A second matrix of the same dimensions
    :return: The product of the two matrices
    """
    size = len(matrix_a)
    matrix_c = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            for k in range(size):
                matrix_c[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return matrix_c


def main():
    size = int(sys.argv[1])
    matrix_a = randomize(size)
    matrix_b = randomize(size)
    matrix_c = multiply(matrix_a, matrix_b)


if __name__ == "__main__":
    main()
