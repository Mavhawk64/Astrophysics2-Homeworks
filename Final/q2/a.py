import sympy as sp

u_p, v, Gamma, theta_prime = sp.symbols('u\' v \\Gamma \\theta\'', real=True)
c = sp.symbols('c', real=True, positive=True)

u_par_p = u_p * sp.cos(theta_prime)
u_perp_p = u_p * sp.sin(theta_prime)

u_par = (u_par_p + v) / (1 + v/c**2 * u_par_p)
u_perp = u_perp_p / (Gamma * (1 + v/c**2 * u_par_p))

print("\\tan\\theta =", sp.latex(sp.simplify(u_perp/u_par)))
