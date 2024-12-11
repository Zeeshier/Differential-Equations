from scipy.integrate import solve_ivp

def growth_model(t, y): return 0.5 * y
sol = solve_ivp(growth_model, [0, 10], [1], t_eval=[i for i in range(11)])
print("Exponential Growth:", sol.y)
