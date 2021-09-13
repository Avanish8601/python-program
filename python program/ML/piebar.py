import matplotlib.pyplot as plt
labels=["one","two","three"]
data=[100,200,300]
plt.pie(data,labels=labels, autopct="%1.1f%%",explode=[0.1,0.0,0.0])
plt.legend()
plt.show()