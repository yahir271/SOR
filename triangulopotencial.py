import matplotlib.pyplot as plt

# Valores de p e iteraciones proporcionados
p_values = [1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2]
iterations = [585, 559, 527, 492, 453, 411, 366, 316, 254, 165, 10000]

# Crear el gráfico con los valores de iteración en cada punto
plt.figure(figsize=(10, 6))
plt.plot(p_values, iterations, marker='o', color='purple', linestyle='-')
plt.xlabel('p',fontsize=22)
plt.ylabel('Iteraciones',fontsize=22)
plt.title('p vs Iteraciones',fontsize=24)
plt.grid(False)

# Añadir los valores de iteración en cada punto
for p, iter_val in zip(p_values, iterations):
    plt.text(p, iter_val, str(iter_val), ha='right', va='bottom', fontsize=14)

plt.show()

