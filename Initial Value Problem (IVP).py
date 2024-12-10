from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def dy_dx(t, y): return -y

sol = solve_ivp(dy_dx, [0, 5], [1], t_eval=[0, 1, 2, 3, 4, 5])
plt.plot(sol.t, sol.y[0], label="y(t)")
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Solution of IVP')
plt.legend()
plt.show()
