import numpy
import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[2,4,8,16]
pf=numpy.polyfit(x,y,2)
print(pf)
model=numpy.poly1d(pf)
print(model)
dev=model.deriv()
print(dev)
predictx=[8,12,15]
plt.plot(predictx,model(predictx))
plt.scatter(predictx,model(predictx),color="black",marker="o",alpha=0.5,label="predict data")
plt.plot(x,y)
plt.scatter(x,y,color="red",marker="o",alpha=0.5,label="Share data")
plt.plot(dev,color="green",alpha=0.5,label="derivation")
plt.xlabel("DAY")
plt.ylabel("SHARE")
plt.title("Share marketing")
plt.legend()
plt.show()