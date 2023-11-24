# Celda 1
import micropip
await micropip.install('ipywidgets')


# Celda 2
import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import interact, widgets

fig, ax = plt.subplots()

# Evalua la función polinómica
def funcion_polinomica(x, A, B, C, D):
    return A*x**3 + B*x**2 + C*x + D

# Dibuja la función polinómica
def dibuja_funcion(A, B, C, D):
    x = np.linspace(-10, 10, 200)
    y = funcion_polinomica(x, A, B, C, D)
    tF = "$y=f(x)=A*x^3+B*x^2+C*x+D$\n$f(x)=$"
    if A == 0.0:
        tF = tF + ""
    else:
        tF = tF + f"{round(A, 1)}$x^3$ + "
    if B == 0.0:
        tF = tF + ""
    else:
        tF = tF + f"{round(B, 1)}$x^2$ + "
    if C == 0.0:
        tF = tF + ""
    else:
        tF = tF + f"{round(C, 1)}$x$ + "
    if D == 0.0:
        tF = tF + ""
    else:
        tF = tF + f"{round(D, 1)}"
    plt.title(tF)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.xticks(range(-10, 10))
    plt.yticks(range(-10, 10))
    plt.xlabel('Eje $X$')
    plt.ylabel('Eje $Y$')
    plt.plot(x, y)
    plt.grid(True)
    plt.plot([0, 0], [10, -10], color='red')
    plt.plot([10, -10], [0, 0], color='red')
    plt.show()

# Cambia el coeficiente
def cambiando(slider, switch):
    if switch is True:
        for value in np.arange(slider.min, slider.max + 0.1, 0.1):
            slider.value = value

# Creando controles
A_slider = widgets.FloatSlider(value=1, min=-10, max=10, step=0.1, description='A:')
B_slider = widgets.FloatSlider(value=1, min=-10, max=10, step=0.1, description='B:')
C_slider = widgets.FloatSlider(value=1, min=-10, max=10, step=0.1, description='C:')
D_slider = widgets.FloatSlider(value=1, min=-10, max=10, step=0.1, description='D:')
A_switch = widgets.ToggleButton(value=False, description='Variando A')
B_switch = widgets.ToggleButton(value=False, description='Variando B')
C_switch = widgets.ToggleButton(value=False, description='Variando C')
D_switch = widgets.ToggleButton(value=False, description='Variando D')

# Creando interacción
interact(dibuja_funcion, A=A_slider, B=B_slider, C=C_slider, D=D_slider)

# Asignando animación
A_switch.observe(lambda change: cambiando(A_slider, change.new), names='value')
B_switch.observe(lambda change: cambiando(B_slider, change.new), names='value')
C_switch.observe(lambda change: cambiando(C_slider, change.new), names='value')
D_switch.observe(lambda change: cambiando(D_slider, change.new), names='value')

# Mostrando controles
g01 = widgets.VBox([A_switch])
g02 = widgets.VBox([B_switch])
g03 = widgets.VBox([C_switch])
g04 = widgets.VBox([D_switch])
g10 = widgets.HBox([g01, g02, g03, g04])
display(g10)