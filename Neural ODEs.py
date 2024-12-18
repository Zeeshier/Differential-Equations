import torch
import torch.nn as nn
from torchdiffeq import odeint
import matplotlib.pyplot as plt


class ODEFunc(nn.Module):
    def __init__(self):
        super(ODEFunc, self).__init__()
        self.linear = nn.Linear(2, 50)
        self.relu = nn.ReLU()
        self.output = nn.Linear(50, 2)

    def forward(self, t, y):
        return self.output(self.relu(self.linear(y)))

y0 = torch.tensor([1.0, 0.0])  
t = torch.linspace(0, 10, 100)  

func = ODEFunc()
solution = odeint(func, y0, t)

plt.plot(t.numpy(), solution[:, 0].detach().numpy(), label='y1')
plt.plot(t.numpy(), solution[:, 1].detach().numpy(), label='y2')
plt.legend()
plt.title("Neural ODE Solution")
plt.xlabel("Time")
plt.ylabel("State")
plt.show()
