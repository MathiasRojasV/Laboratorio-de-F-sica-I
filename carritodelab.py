#Este codigo tiene como objetivo ilustrar el uso de herramientas digitales para la simulacion o creacion de graficas en el laboratorio 
#de fisica I, para usar correctamente, cambie los parametros de las lineas 8 a la 12 a su gusto, y comience la ejecucion del programa.


import numpy as np
import matplotlib.pyplot as plt

M = 1.0     # masa del carrito (kg)
m = 0.5     # masa del contrapeso (kg)
h = 1       # altura desde la que cae el contrapeso (m)
d = 0.8     # largo maximo de la mesa (m)
g = 9.77589 # gravedad en Costa Rica (m/s^2)
a = m*g / (M + m) # aceleracion

dt = 0.01
t_max = 5
t = np.arange(0, t_max, dt)

x_carrito = []  
y_peso = []      
v = 0
x = 0
y = h

for _ in t:
    if y > 0 and x < d:
        x += v*dt + 0.5*a*dt**2
        v += a*dt
        y = h-x  
    else:
        a = 0
        v = 0
        x = min(x,d)
        y = max(h-x, 0)

    x_carrito.append(x)
    y_peso.append(y)

plt.plot(t, x_carrito, label="Posición del carrito (m)")
plt.plot(t, y_peso, label="Altura del contrapeso (m)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Posición (m)")
plt.title("Simulación carrito y contrapeso con límite de mesa")
plt.legend()
plt.grid()
plt.show()
