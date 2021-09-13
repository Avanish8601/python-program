import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("pandas.csv")
print(data)
#plt.scatter(data["name"],data["obtained"],color="green",marker='o')
plt.bar(data["name"],data["obtained"],color="green",)
plt.xlabel("name",color="green")
plt.ylabel("marks",color="green")
plt.title("marks",color="red")
plt.show()