import numpy as np
import matplotlib.pyplot as plt
import time

def lagrange_interp(x_p, y_p, x_eval):
    n = len(x_p)
    val = 0
    for i in range(n):
        num, den = 1, 1
        for j in range(n):
            if i != j:
                num *= (x_eval - x_p[j])
                den *= (x_p[i] - x_p[j])
        val += y_p[i] * (num / den)
    return val

x_puntos = np.array([2.0, 4.0, 6.0, 8.0])
y_puntos = np.array([2500, 2300, 2150, 2050])
x_target = 5.0

inicio = time.perf_counter()
y_target = lagrange_interp(x_puntos, y_puntos, x_target)
tiempo_total = time.perf_counter() - inicio

# Ventana 1: Gráfica
plt.figure("Ejercicio 3 - Gráfica", figsize=(8, 5))
x_plot = np.linspace(2.0, 8.0, 100)
y_plot = [lagrange_interp(x_puntos, y_puntos, x) for x in x_plot]
plt.plot(x_puntos, y_puntos, 'ko', label='Datos Aeronave')
plt.plot(x_plot, y_plot, 'm-', label='Polinomio Lagrange')
plt.plot(x_target, y_target, 'rs', label=f'Estimación x={x_target}')
plt.title("Predicción de Consumo de Combustible")
plt.xlabel("Altitud (km)"); plt.ylabel("Consumo (kg/h)")
plt.legend(); plt.grid(True)
plt.show(block=False)

# Ventana 2: Tabla
fig, ax = plt.subplots(num="Ejercicio 3 - Tabla", figsize=(8, 4))
ax.axis('off')
ax.table(cellText=[[x_target, round(y_target, 4), f"{tiempo_total:.6e} s"]], 
         colLabels=['Punto x', 'Consumo (kg/h)', 'Tiempo CPU'], loc='center')
plt.show()