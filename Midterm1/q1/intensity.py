import sympy as sp

# mu(R) = mu_e + 2.5 * b_n * ((R/R_e)^(1/n)-1)
R = sp.symbols("R", positive=True, real=True)
n = 4
b_n = 2 * n - 0.33
mu_e = 20.4  # mag/arcsec^2
R_e = 110  # arcsec

mu_R = mu_e + 2.5 * b_n * ((R / R_e) ** (1 / n) - 1)
print(mu_R)
