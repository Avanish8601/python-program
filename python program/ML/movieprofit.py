import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("movie.csv")
#print(data)
f=1000
data["X"]=data["X"]//f
data["Y"]=data["Y"]//f
print(data)
plt.pie(data["X"],labels=data["Y"],autopct="%1.0f%%")
plt.title("Movie profit pie")
plt.show()
brange=["1000-10000","10000-50000","50000-100000","100000-130000"]
budget= 100000
if budget >1000 and budget<10000:
    d1=data[(data["X"] >= 1000) & (data["X"] <= 10000)]
    print(d1)
    label=["0-50000","1500000-5000000","5000000-1500000","15000000-101000000"]

    count=[0,0,0,0]
    for i in d1["Y"]:
        if i<50000:
            count[0]+=1
        elif i<100000:
            count[1]+=1
        elif i<500000:
            count[2]+=1
        elif i<1000000:
            count[3]+=1
    plt.pie(count,labels=label,autopct="%1.0f%%")
    plt.title("budget 1000 to 10000")
    plt.show()
elif budget >=10000 and budget<50000:

    d1=data[(data["X"] >= 10000) & (data["X"] <= 50000)]
    print(d1)
    label=["0-50000","1500000-5000000","5000000-1500000","15000000-101000000"]
    count=[0,0,0,0]
    for i in d1["Y"]:
        if i<50000:
            count[0]+=1
        elif i<100000:
            count[1]+=1
        elif i<500000:
            count[2]+=1
        elif i<1000000:
            count[3]+=1
    plt.pie(count,labels=label,autopct="%1.0f%%")
    plt.title("budget 10000 to 50000")
    plt.show()

elif budget >50000 and budget<100000:
    d1=data[(data["X"] >= 50000) & (data["X"] <= 100000)]
    print(d1)
    label = ["0-50000", "1500000-5000000", "5000000-1500000", "15000000-101000000"]
    count=[0,0,0,0]
    for i in d1["Y"]:
        if i<50000:
            count[0]+=1
        elif i<100000:
            count[1]+=1
        elif i<500000:
            count[2]+=1
        elif i<1000000:
            count[3]+=1
    plt.pie(count,labels=label,autopct="%1.0f%%")
    plt.title("budget 50000 to 100000")
    plt.show()

elif budget >=100000 and budget<130000:
    d1=data[(data["X"] >= 100000) & (data["X"] <= 130000)]
    print(d1)
    label = ["0-50000", "1500000-5000000", "5000000-1500000", "15000000-101000000"]


    count=[0,0,0,0]
    for i in d1["Y"]:
        if i<50000:
            count[0]+=1
        elif i<100000:
            count[1]+=1
        elif i<500000:
            count[2]+=1
        elif i<1000000:
            count[3]+=1
    plt.pie(count,labels=label,autopct="%1.0f%%")
    plt.title("budget 100000 to 130000")
    plt.show()