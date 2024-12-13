import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x + y

def euler_method(f, x0, y0, h, x_end):
    x_values = np.arange(x0, x_end + h, h)
    y_values = np.zeros(len(x_values))
    y_values[0] = y0  

    for i in range(1, len(x_values)):
        y_values[i] = y_values[i - 1] + h * f(x_values[i - 1], y_values[i - 1])
    return x_values, y_values

x0 = 0      
y0 = 1     
h = 0.1     
x_end = 2    

x_vals, y_vals = euler_method(f, x0, y0, h, x_end)

plt.plot(x_vals, y_vals, label="Euler's Method", marker='o')
plt.title("Euler's Method for Solving ODE")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()
