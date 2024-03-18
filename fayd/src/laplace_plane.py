import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import pdb

def func_hs(func):
    x = np.linspace(-10, 10, 200)
    a, w = np.meshgrid(x, x)
    #
    Hs = func(a, w)
    return Hs

def plot3D(Hs):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = Hs.real
    y = Hs.imag
    z = 20*np.log10(np.absolute(Hs))
    surface = ax.plot_surface(x, y, z, cmap='viridis')
    #
    plt.show()
#
hs_pb_o1 = lambda a, w: 1 / (a + 1j*w + 1)
hs_pb_o2 = lambda a, w: 1 / ((a + 1j*w)**2 + (a + 1j*w) + 1)
hs_pa_o1 = lambda a, w: (a + 1j*w) / (a + 1j*w + 1)
hs_pa_o2 = lambda a, w: ((a + 1j*w)**2) / ((a + 1j*w)**2 + (a + 1j*w) + 1)
#
hs = func_hs(hs_pb_o1)
plot3D(hs)
#
hs = func_hs(hs_pb_o2)
plot3D(hs)
#
hs = func_hs(hs_pa_o1)
plot3D(hs)
#
hs = func_hs(hs_pa_o2)
plot3D(hs)