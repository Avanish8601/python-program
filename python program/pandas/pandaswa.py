import pandas as pd
run={"sachin": 100,"virat":50,"dhoni":67}
wicket={"panda":2,"chahal":3,"bumrah":1}
data=[run,wicket]
Index=["run","wicket"]
df=pd.DataFrame(data,Index)
print(df)
df.to_csv("E:\python program\score.csv")
df.to_excel("E:\python program\score.xlsx)

