import numpy as np
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[3,5,7,9,11]
df=np.polyfit(x,y,2)
print(df)
model=np.poly1d(df)
print(model)
derv=model.deriv()
print(derv)
predictx=[9,13,7]
plt.scatter(predictx,model(predictx),color="green",marker="o")
plt.scatter(x,y,color="black")
plt.plot(x,y)
plt.plot(predictx,model(predictx),color="red")
plt.show()
codd