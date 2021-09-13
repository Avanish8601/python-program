import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,4*np.pi,0.1)

y=np.sin(x)
plt.plot(x,y,color="red",marker="o")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

#3D graph of sin angle#######

"""import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,20,0.1)
y=np.sin(x)
#z=x+y
fig=plt.figure(figsize=(10,10))
ax=plt.gca(projection='3d')
ax.set_xlabel("X",fontsize=20)
ax.set_ylabel("Y",fontsize=20)
#ax.set_zlabel("z",fontsize=20)
plt.show()"""