import matplotlib.pyplot as plt
x=[3,7,4,9,5]
y=[2,8,14,6,9]
#plt.scatter(x,y,color='green',marker='o')
#plt.plot(x,y,color='green',marker='o')
plt.xlabel("X")
plt.ylabel("Y")
plt.bar(x,y,color='green')
plt.title("XandY")
plt.show()