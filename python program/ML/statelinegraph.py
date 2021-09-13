import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return 2*x+5    #y=mx+c
x=[1,2,3,4,5]
y=[]
for i in range (len(x)):
    y.append(f(x[i]))
print(y)
plt.plot(x,y,color="red",marker="o")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()

