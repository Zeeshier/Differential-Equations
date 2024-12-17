import numpy as np
import matplotlib.pyplot as plt

L = 1.0        
T = 0.1         
nx = 20         
nt = 1000       
alpha = 0.01     

dx = L / (nx - 1)         
dt = T / nt               
r = alpha * dt / dx**2    

u = np.zeros((nt, nx))    
u[0, :] = np.sin(np.pi * np.linspace(0, L, nx))  
u[:, 0] = 0              
u[:, -1] = 0              

for n in range(0, nt-1):
    for i in range(1, nx-1):
        u[n+1, i] = u[n, i] + r * (u[n, i-1] - 2*u[n, i] + u[n, i+1])

plt.figure(figsize=(8, 5))
for n in range(0, nt, nt // 10):
    plt.plot(np.linspace(0, L, nx), u[n, :], label=f"t={n*dt:.3f}")
plt.title("Heat Equation Solution (Explicit Finite Difference)")
plt.xlabel("x (Length)")
plt.ylabel("u(x, t) (Temperature)")
plt.legend()
plt.grid()
plt.show()
