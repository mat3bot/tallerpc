####Celda 1####
import micropip
await micropip.install('ipywidgets')


####Celda 2####
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, widgets

# Subproceso: graficar f(x)=Ax^2 + Bx + C
def funcion_cuadratica(valor_A, valor_B, valor_C):
    Lista_x = np.linspace(-10, 10, 1000)
    Lista_y = valor_A*Lista_x*Lista_x + valor_B*Lista_x + valor_C
    plt.plot(Lista_x, Lista_y)
    plt.title('f(x)=Ax^2 + Bx + C')
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.grid(True)
    plt.show()

# Inicio
a = widgets.IntSlider(value=1, min=-10, max=10, step=1, description='Valor A:')
b = widgets.IntSlider(value=1, min=-10, max=10, step=1, description='Valor B:')
c = widgets.IntSlider(value=1, min=-10, max=10, step=1, description='Valor C:')

# Interacción
interact(funcion_cuadratica, valor_A=a, valor_B=b, valor_C=c)

