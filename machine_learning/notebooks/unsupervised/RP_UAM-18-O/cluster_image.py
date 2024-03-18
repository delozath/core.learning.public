from mpl_toolkits.mplot3d import Axes3D
from skimage.color        import rgb2grey

import numpy             as np
import matplotlib.pyplot as plt

im = plt.imread('../../images/Chess_Board.png')
im_g = rgb2grey(im)

x  = np.linspace(0, 1, im_g.shape[0])
y  = np.linspace(0, 1, im_g.shape[1])

x,y  = np.meshgrid( x,y )

ax = plt.figure(figsize=(8,8)).add_subplot(111, projection='3d');

ax.plot_surface( x, y, im_g.T, 
                   cmap='inferno',
                   linewidth=2, 
                   antialiased=False )
ax.set_aspect('equal')
plt.show()

