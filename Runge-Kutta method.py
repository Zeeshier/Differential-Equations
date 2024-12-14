import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x + y

def runge_kutta(f, x0, y0, h, x_end):
    x_values = np.arange(x0, x_end + h, h)
    y_values = np.zeros(len(x_values))
    y_values[0] = y0  # Initial condition

    for i in range(1, len(x_values)):
        x_n = x_values[i - 1]
        y_n = y_values[i - 1]

        k1 = h * f(x_n, y_n)
        k2 = h * f(x_n + h / 2, y_n + k1 / 2)
        k3 = h * f(x_n + h / 2, y_n + k2 / 2)
        k4 = h * f(x_n + h, y_n + k3)

        y_values[i] = y_n + (k1 + 2*k2 + 2*k3 + k4) / 6

    return x_values, y_values

x0 = 0       
y0 = 1       
h = 0.1      
x_end = 2    

x_vals, y_vals = runge_kutta(f, x0, y0, h, x_end)

plt.plot(x_vals, y_vals, label="RK4 Method", marker='o', color='blue')
plt.title("Runge-Kutta 4th Order Method")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()
