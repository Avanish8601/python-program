import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("probability.csv")
#print(data)
boys=data["boys"]
mark1=data["marks1"]
mark2=data["marks2"]
#print(boys,mark1,mark2)
plt.pie(mark1,labels=boys, autopct="%1.0F%%")
plt.legend()
plt.show()
plt.pie(mark2,labels=boys, autopct="%1.0F%%")
plt.legend()
plt.show()
data["mark1-mark2"]=data["marks2"] - data["marks1"]
benifit=0
notbenifit=0
for i in data["mark1-mark2"]:
    if i>0:
        benifit+=1
    else:
        notbenifit+=1
print(benifit,notbenifit)
plt.pie([benifit,notbenifit],labels=[benifit,notbenifit],autopct="%1.0f%%")
plt.show()
range=["15-20","20-25","25-30","30-35","35-40"]
n=[0,0,0,0,0]
for i in data["marks1"]:
    if i<=15:
        n[0]+=1
    elif i<=20:
        n[1]+=1
    elif i<=25:
        n[2]+=1
    elif i<=30:
        n[3]+=1
    elif i<=35:
        n[4]+=1
plt.pie(n,labels=range,autopct="%1.0f%%")
plt.show()
