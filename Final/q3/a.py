from math import log10


def logT(x):
    return 9.9551 - 3.3674 * x + 0.4794 * x**2 + 0.3676 * x**3 - 0.1013 * x**4


print('{:.2e}'.format(10**logT(log10(1.5))))
