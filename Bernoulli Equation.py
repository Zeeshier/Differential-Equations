from sympy import dsolve, Eq, Function, symbols

x = symbols('x')
y = Function('y')
ode = Eq(y(x).diff(x) + y(x), x**2 * y(x)**2)
solution = dsolve(ode, y(x))
print("Solution:", solution)
