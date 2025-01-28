import sympy as sp

# Define the variables
y = sp.symbols('y', real=True)
t = sp.symbols('t', real=True)
x, a, b = sp.symbols('x a b', real=True, positive=True)

# Define the equation
ellipse_eq = sp.Eq((x*sp.cos(t) + y*sp.sin(t))**2 / a**2 +
                   (x*sp.sin(t) - y*sp.cos(t))**2 / b**2, 1)

# solve the equation for y

y_solutions = sp.solve(ellipse_eq, y)

print(len(y_solutions), "\n\n", y_solutions, "\n\n")

for i in range(len(y_solutions)):
    print("y = ", sp.latex(y_solutions[i].simplify()))

green = y_solutions[1].simplify()

# find dx/dy
dydx = sp.diff(green, x)

dxdy = 1/dydx

print("\n\n", sp.latex(dxdy.simplify()), "\n\n")

# solve x for dxdy = 0
dxdy_eq = sp.Eq(dxdy, 0)

x_solutions = sp.solve(dxdy_eq, x)

print(len(x_solutions), "\n\n", x_solutions, "\n\n")

for i in range(len(x_solutions)):
    print("x = ", sp.latex(x_solutions[i].simplify()))
