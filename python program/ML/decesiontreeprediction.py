import pandas as pd
from sklearn.tree import DecisionTreeClassifier
data=pd.read_csv("show.csv")
print(data)
d={'pass':1,'fail':0}
data['result']=data['result'].map(d)
#print(data['result'])
feature=['physics','chemistry','math']
x=data[feature]
y=data['result']
#print(x)
#print(y)
dtree=DecisionTreeClassifier()
dtree=dtree.fit(x,y)
print(dtree.predict([[45,55,50]]))
print("0 means fail")
print("1 means pass")
