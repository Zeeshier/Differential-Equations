import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def f(t, y):
    return -2 * y + t

t_span = (0, 10)  
y0 = [1]          

solution = solve_ivp(f, t_span, y0, method='RK45', rtol=1e-6, atol=1e-8)

t = solution.t
y = solution.y[0]

plt.plot(t, y, label="Numerical Solution (RK45)", marker='o', color='blue')
plt.title("Solution of ODE using Dormand-Prince Method")
plt.xlabel("t")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()
