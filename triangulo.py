import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la simulación
N = 100  # Tamaño de la malla
max_iterations = 10000  # Número máximo de iteraciones
tolerance = 1e-2  # Tolerancia para la convergencia
A = 1
p = 2  # Parámetro SOR

# Crear una malla de potencial
V = np.zeros((N, N))
# Crear una matriz de cargas
q = np.zeros((N, N))

# Coordenadas de los vértices del triángulo
vertice1 = (20, 20)
vertice2 = (20, 60)
vertice3 = (70, 40)

# Asignar cargas a las placas del triángulo con franjas de carga más gruesas
# Placa 1 (positiva) entre vértices 1 y 2
for i in range(20, 61):
    q[i, 20] = 1  # Carga positiva en una franja de 3 filas

# Placa 2 (negativa) entre vértices 2 y 3
for i in range(20, 41):
    x = int((5*i)/2 - 30)
    q[i, x] = -1  # Carga negativa en una franja de 3 columnas

# Placa 3 (negativa) entre vértices 1 y 3
for i in range(40, 61):
    x = int((-5*i)/2 + 170)
    q[i, x] = -1  # Carga negativa en una franja de 3 columnas

# Condiciones de frontera en los extremos de la caja
V[0, :] = 0
V[N-1, :] = 0
V[:, 0] = 0
V[:, N-1] = 0

# Método de relajación
for iteration in range(max_iterations):
    V_old = V.copy()

    # Actualizar el potencial en cada punto, excepto en las posiciones de las cargas
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            # Potencial en el resto del espacio
            V[i, j] = 0.25 * (V[i + 1, j] + V[i - 1, j] + V[i, j + 1] + V[i, j - 1]) + A * q[i, j]
            V[i, j] = V_old[i, j] + p * (V[i, j] - V_old[i, j])  # SOR corregido

    # Comprobar la convergencia
    if np.max(np.abs(V[1:-1, 1:-1] - V_old[1:-1, 1:-1])) < tolerance:
        print(f"Convergido después de {iteration + 1} iteraciones.")
        break

# Cálculo del campo eléctrico a partir del gradiente del potencial
Ey, Ex = np.gradient(-V)

# Visualización del potencial, campo eléctrico y placas
x = np.linspace(0, N - 1, N)
y = np.linspace(0, N - 1, N)
Y, X = np.meshgrid(x, y)

plt.figure(figsize=(10, 8))

# Graficar las líneas de equipotencial
contour = plt.contour(X, Y, V, levels=50, cmap='coolwarm', linewidths=1)
plt.colorbar(contour).set_label("Potencial (V)", fontsize=20)
#plt.clabel(contour, inline=True, fontsize=10, fmt='%1.0f')

# Graficar el campo eléctrico como flechas
#plt.quiver(X, Y, Ex, Ey, color='midnightblue', alpha=0.5, scale=20)

# Graficar las placas como líneas
plt.plot([vertice1[1], vertice2[1]], [vertice1[0], vertice2[0]], color='red', linewidth=2, label="+q")
plt.plot([vertice2[1], vertice3[1]], [vertice2[0], vertice3[0]], color='black', linewidth=2, label="-q")
plt.plot([vertice3[1], vertice1[1]], [vertice3[0], vertice1[0]], color='black', linewidth=2, label="-q")

# Ajustes de la gráfica
plt.title('Líneas equipotenciales',fontsize=24)
plt.xlabel('x',fontsize=22)
plt.ylabel('y',fontsize=22)
plt.legend()
plt.grid(False)
plt.axis('equal')
plt.show()
