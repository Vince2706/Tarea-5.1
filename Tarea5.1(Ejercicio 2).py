import numpy as np
import matplotlib.pyplot as plt
import time

def lagrange_interp(x_p, y_p, x_eval):
    n = len(x_p)
    res = 0
    for i in range(n):
        L = 1
        for j in range(n):
            if i != j: L *= (x_eval - x_p[j]) / (x_p[i] - x_p[j])
        res += y_p[i] * L
    return res

x_puntos = np.array([1.0, 2.5, 4.0, 5.5])
y_puntos = np.array([85, 78, 69, 60])
x_target = 3.0

inicio = time.perf_counter()
y_target = lagrange_interp(x_puntos, y_puntos, x_target)
tiempo_total = time.perf_counter() - inicio

# Ventana 1: Gráfica
plt.figure("Ejercicio 2 - Gráfica", figsize=(8, 5))
x_range = np.linspace(1.0, 5.5, 100)
y_range = [lagrange_interp(x_puntos, y_puntos, xi) for xi in x_range]
plt.plot(x_puntos, y_puntos, 'ro', label='Datos medidos')
plt.plot(x_range, y_range, 'g--', label='Polinomio Lagrange')
plt.plot(x_target, y_target, 'bs', label=f'Estimación x={x_target}')
plt.title("Perfil de Temperatura en Motor")
plt.xlabel("Profundidad (cm)"); plt.ylabel("Temperatura (°C)")
plt.legend(); plt.grid(True)
plt.show(block=False)

# Ventana 2: Tabla
fig, ax = plt.subplots(num="Ejercicio 2 - Tabla", figsize=(8, 4))
ax.axis('off')
ax.table(cellText=[[x_target, round(y_target, 4), f"{tiempo_total:.6e} s"]], 
         colLabels=['Punto x', 'Temperatura (°C)', 'Tiempo CPU'], loc='center')
plt.show()