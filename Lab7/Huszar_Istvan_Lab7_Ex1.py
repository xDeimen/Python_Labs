import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def f(x, y):
    r = np.sqrt(x**2 + y**2)
    return np.sqrt(r**2)*np.sinc(r/np.pi)


x = np.linspace(-10, 10, 500)
y = np.linspace(-10, 10, 500)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

