import sympy as sp
from math import log10

T, x = sp.symbols('\\log_{10}(T) x', real=True, positive=True)


def f(x):
    return 9.9551 - 3.3674 * x + 0.4794 * x**2 + 0.3676 * x**3 - 0.1013 * x**4 - log10(12*10**9)


def f_prime(x):
    return -3.3674 + 2 * 0.4794 * x + 3 * 0.3676 * x**2 - 4 * 0.1013 * x**3


def newton_raphson(x0, tol=1e-10, max_iter=100):
    x = x0
    for i in range(max_iter):
        x_new = x - f(x) / f_prime(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise ValueError("Newton-Raphson method did not converge")


x0 = 0.1
x_solution = newton_raphson(x0)
print(10 ** x_solution)
