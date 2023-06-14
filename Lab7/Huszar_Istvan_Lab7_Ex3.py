import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definirea funcției Z(x, y) - suprafața sinusoidală
def Z(x, y, t):
    return np.sin(np.sqrt(x**2 + y**2 + t))

# Generarea valorilor pentru x, y și t
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
t = np.linspace(0, 10, 100)

# Crearea gridului de valori pentru x, y și t
X, Y, T = np.meshgrid(x, y, t)

# Calcularea valorilor funcției Z pentru fiecare triplet (x, y, t)
Z_values = Z(X, Y, T)

# Crearea graficului 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Inițializarea obiectului de suprafață
surface = ax.plot_surface(X[:,:,0], Y[:,:,0], Z_values[:,:,0], cmap='viridis')

# Funcție pentru actualizarea animației
def update_plot(frame):
    ax.clear()
    surface = ax.plot_surface(X[:,:,frame], Y[:,:,frame], Z_values[:,:,frame], cmap='viridis')

# Generarea animației
ani = plt.FuncAnimation(fig, update_plot, frames=len(t), interval=100)

# Afișarea animației
plt.show()