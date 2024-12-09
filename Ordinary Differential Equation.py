from sympy import symbols, Function, dsolve, Eq

x = symbols('x')
y = Function('y')
ode = Eq(y(x).diff(x), y(x))
solution = dsolve(ode, y(x))
print(solution)  
