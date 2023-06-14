import numpy as np
import matplotlib.pyplot as plt

def F1(x):
    return x**3 - 3*x

def F2(x):
    return 1/(x+1) + 3/x - 2/(x-1)

x = np.linspace(-300, 300, 1000)
y1 = F1(x)
y2 = F2(x)
plt.plot(x, y1, label='F1(x)')
plt.plot(x, y2, label='F2(x)')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
