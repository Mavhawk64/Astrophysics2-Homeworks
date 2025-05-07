import sympy as sp

c, D, e, B, m_e, n_e, omega = sp.symbols("c D e B m_e n_e \\omega")

w_pe = sp.sqrt(4 * sp.pi * n_e * e**2 / m_e)
w_Be = e * B / m_e * c
t_t = D / c

n_r_p = sp.sqrt(1 - (w_pe / omega) ** 2 * (1 + w_Be / omega) ** -1)
n_r_m = sp.sqrt(1 - (w_pe / omega) ** 2 * (1 - w_Be / omega) ** -1)

n_r_p = sp.simplify(n_r_p)
n_r_m = sp.simplify(n_r_m)

dn_r_p = sp.simplify(sp.diff(n_r_p, omega))

# dn_r_m = sp.diff(n_r_m, omega)

t_d_p = sp.simplify(t_t * (-1 + (n_r_p + omega * dn_r_p)))
# t_d_m = t_t * (-1 + (n_r_m + omega * sp.diff(n_r_m, omega)))

print(sp.latex(t_d_p))
