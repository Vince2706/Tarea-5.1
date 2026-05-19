import numpy as np
import matplotlib.pyplot as plt
import time

# 1. Implementación de Lagrange
def lagrange_interp(x_p, y_p, x_eval):
    n = len(x_p)
    resultado = 0
    for i in range(n):
        termino = y_p[i]
        for j in range(n):
            if i != j:
                termino *= (x_eval - x_p[j]) / (x_p[i] - x_p[j])
        resultado += termino
    return resultado

# Datos del ejercicio
x_puntos = np.array([0.5, 1.0, 1.5, 2.0])
y_puntos = np.array([1.2, 2.3, 3.7, 5.2])
x_target = 1.25

# 2. Ajuste y Tiempo de procesamiento
inicio = time.perf_counter()
y_target = lagrange_interp(x_puntos, y_puntos, x_target)
fin = time.perf_counter()
tiempo_total = fin - inicio


# Ventana 1: Gráfica de la aproximación
plt.figure("Ejercicio 1 - Gráfica", figsize=(8, 5))
x_curva = np.linspace(min(x_puntos), max(x_puntos), 100)
y_curva = [lagrange_interp(x_puntos, y_puntos, val) for val in x_curva]
plt.plot(x_puntos, y_puntos, 'ro', label='Datos originales')
plt.plot(x_curva, y_curva, 'b-', label='Polinomio Lagrange')
plt.plot(x_target, y_target, 'gs', label=f'Estimación x={x_target}')
plt.title("Interpolación de Lagrange: Deformación en Viga")
plt.xlabel("Posición (m)"); plt.ylabel("Deformación (mm)")
plt.legend(); plt.grid(True)
plt.show(block=False)

# Ventana 2: Tabla de Resultados y Error
fig, ax = plt.subplots(num="Ejercicio 1 - Tabla", figsize=(8, 4))
ax.axis('off')
res_data = [[x_target, round(y_target, 4), f"{tiempo_total:.6e} s"]]
ax.table(cellText=res_data, colLabels=['Punto x', 'Deformación (mm)', 'Tiempo CPU'], loc='center', cellLoc='center')
plt.show()