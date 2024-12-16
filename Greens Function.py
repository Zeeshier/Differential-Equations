import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def greens_function(x, xi):
    if x < xi:
        return np.sinh(x) * np.sinh(1 - xi) / np.sinh(1)
    else:
        return np.sinh(xi) * np.sinh(1 - x) / np.sinh(1)

def f(x):
    return np.exp(x)

def u(x):
    integrand = lambda xi: greens_function(x, xi) * f(xi)
    result, _ = quad(integrand, 0, 1)  
    return result

x_values = np.linspace(0, 1, 100)
u_values = [u(x) for x in x_values]

plt.plot(x_values, u_values, label="Solution u(x)", color='blue')
plt.title("Solution of ODE using Green's Function")
plt.xlabel("x")
plt.ylabel("u(x)")
plt.legend()
plt.grid()
plt.show()
