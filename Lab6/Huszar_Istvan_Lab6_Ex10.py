import numpy as np
import matplotlib.pyplot as plt

# Definirea funcției Z(x, y)
def Z(x, y):
    return y**2 - x**2

# Generarea valorilor pentru x și y
x = np.linspace(-100, 100, 1000)
y = np.linspace(-20, 20, 1000)
X, Y = np.meshgrid(x, y)

# Calcularea valorilor funcției Z pentru fiecare pereche (x, y)
Z_values = Z(X, Y)

# Crearea graficului izoplan
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z_values, cmap='viridis')

# Setarea etichetelor pentru axe
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Z')

# Afișarea graficului
plt.show()