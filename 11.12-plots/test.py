# NOTE: There exists a vast variety of algorithms for scientific computation,
#       which we do not have nearly enough time to explain. However, these
#       algorithms are already implemented by third-party libraries, which we
#       can simply import and use from within Python.
import numpy as np
from scipy import linalg

# NOTE: To solve the system of two equations:
#        2x + 3y = 6
#        4x + 9y = 15
lhs = np.array([[2, 3], [4, 9]])
rhs = np.array([6, 15])
print(linalg.solve(lhs, rhs))

# NOTE: There exist problems which, to the best of our knowledge, cannot be
#       solved quickly by computers. Instead, many scientific computations are
#       based on numerical approximations using a finite number of samples.
#       To integrate f(x) = x^2 dx from 0 to 2:
from scipy import integrate

def f(x):
    return x ** 2

# NOTE: ...this returns two values, both the actual value of the definite
#       integral and a expected margin of error, essentially how confident
#       SciPy is in its approximation of the solution.
print(integrate.quad(f, 0, 2))

# NOTE: If we want to visualize any of this data, the Matplotlib library
#       can create graphical windows, images, PDFs, etc. based on NumPy
#       arrays.
import matplotlib.pyplot as plt
# x = np.arange(10)
# y = np.arange(10) ** 2
# plt.plot(x, x, label = "y = x")
# plt.plot(x, y, label = "y = x^2")
# plt.legend()

# NOTE: Here, we generate random data that looks sort of like y = x^2, and we
#       define a quadratic function g that we wish to fit to this data:
from scipy import optimize

def g(x, a, b, c):
    return a * x ** 2 + b * x + c

x = np.arange(100)
y = (x + np.random.randint(-10, 10, 100)) ** 2

# NOTE: ...the SciPy module can then determine the approximate best values
#       for the coefficients a, b, and c, which we can plug back into g
#       in order to determine the y values of the fitted curve:
coeffs, _ = optimize.curve_fit(g, x, y)
fitted = np.array([g(num, coeffs[0], coeffs[1], coeffs[2]) for num in x])

plt.scatter(x, y)
plt.plot(x, fitted, color="red")
plt.savefig("figure.png")
plt.show()