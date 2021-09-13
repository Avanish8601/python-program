import numpy as np
import matplotlib.pyplot as plt
def f(x):
    sum=0
    for i in range(len(x)):

        sum+=x[i]**2
    sum=sum+1
    return sum
a=[1,2,3,4,5]
b=f(a)
print(b)

"""pf=np.polyfit(x,y,2)
print(pf)
model=np.poly1d(pf)
print(model)
plt.scatter(x,y,color="red",marker="o")
plt.plot(x,y)
plt.show()"""