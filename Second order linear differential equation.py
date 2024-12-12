from sympy import dsolve, Eq, Function, symbols

# Define the variables and function
x = symbols('x')
y = Function('y')

# Define the second-order ODE
ode = Eq(y(x).diff(x, 2) - 3*y(x).diff(x) + 2*y(x), 0)

# Solve the ODE
solution = dsolve(ode, y(x))

# Print the solution
print("Solution:", solution)
