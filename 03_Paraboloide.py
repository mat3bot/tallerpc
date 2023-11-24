# Celda 1
import micropip
await micropip.install('ipywidgets')


# Celda 2
import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import interact, widgets
from mpl_toolkits import mplot3d

fig = plt.figure(figsize =(14, 9))

#fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Evalua la función paraboloide
def funcion_paraboloide(x, y, A, B, C, D):
    return A*x*x + B*y*y + C*x*y + D

# Dibuja la función paraboloide
def dibuja_funcion(A, B, C, D):
    ax = plt.axes(projection ='3d')
    x = np.outer(np.linspace(-10, 10, 32), np.ones(32))
    y = x.copy().T
    z = funcion_paraboloide(x, y, A, B, C, D)
    ax.plot_surface(x, y, z)
    ax.set_zlim(-10, 10)
    tF = "$y=f(x)=A*x^2+B*y^2+C*xy+D$\n$f(x)=$"
    if A == 0.0:
        tF = tF + ""
    else:
        tF = tF + f"{round(A, 1)}$x^2$ + "
    if B == 0.0:
        tF = tF + ""
    else:
        tF = tF + f"{round(B, 1)}$y^2$ + "
    if C == 0.0:
        tF = tF + ""
    else:
        tF = tF + f"{round(C, 1)}$xy$ + "
    if D == 0.0:
        tF = tF + ""
    else:
        tF = tF + f"{round(D, 1)}"
    plt.title(tF)
    plt.xlabel('Eje $X$')
    plt.ylabel('Eje $Y$')
    
    #plt.plot(x, y)
    #plt.grid(False)
    plt.show()

# Creando controles
A_slider = widgets.FloatSlider(value=1, min=-5, max=5, step=0.1, description='A:')
B_slider = widgets.FloatSlider(value=1, min=-5, max=5, step=0.1, description='B:')
C_slider = widgets.FloatSlider(value=1, min=-5, max=5, step=0.1, description='C:')
D_slider = widgets.FloatSlider(value=1, min=-5, max=5, step=0.1, description='D:')

# Creando interacción
interact(dibuja_funcion, A=A_slider, B=B_slider, C=C_slider, D=D_slider)
