import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
def f(x,y):
    return 2*x*x+2*y*y+4
error=0.0001
x=np.linspace(start=-4,stop=4,num=200)
y=np.linspace(start=-4,stop=4,num=200)
x,y=np.meshgrid(x,y)
fig=plt.figure(figsize=(16,12))
ax=fig.gca(projection='3d')
ax.set_xlabel("X",fontsize=20)
ax.set_ylabel("Y",fontsize=20)
ax.set_zlabel("Z",fontsize=20)
ax.plot_surface(x,y,f(x,y),cmap=cm.hot,alpha=0.5)
plt.show()


