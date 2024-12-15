from sympy import symbols, laplace_transform, exp, sin

t, s = symbols('t s')
f = exp(-2 * t) * sin(t)

F = laplace_transform(f, t, s)
print("Laplace Transform:", F)
