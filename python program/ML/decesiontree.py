import pandas as pd
from sklearn.tree import  DecisionTreeClassifier
df=pd.read_csv("show.csv")
d={"A":3,"B":2,"C":1}
df['grade']=df['grade'].map(d)
print(d)
d={'pass':1,'fail':0}
df['result']=df['result'].map(d)
features=['physics','chemistry','math','grade']
x=df[features]
y=df['result']
print(x)
print(y)
dtree=DecisionTreeClassifier()
dtree=dtree.fit(x,y)
print(dtree.predict([[41,70,70,3]]))
print("1 means 'pass'")
print("0 means 'fail'")