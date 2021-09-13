import pandas as pd
data=pd.read_csv("bankdetail.csv")
def checkaccno(data,account):
    t=False
    if account in list(data['account']):
        t=True
    return t

def newac(data):
    name=input("enter name:")
    newac=int(input("enter new account no:"))
    if checkaccno(data,newac):

        print("accoun'/t number already exist")

        return data

    bal=int(input("enter opening balance ammount:"))
    new={'name':name,'account':newac,'balance':bal,'status':open}
    data=data.append(new, ignore_index= True)
    print(data)
    print("account create sucessfull:")
    return data

def deposite(data):
    ano=int(input("enter account no:"))
    query=data[data['account']==ano]
    dep=int(input("enter amount:"))
    reqindex=query.index[0]
    data.loc[reqindex,['balance']] += dep
    #data.to_csv("bank1.csv",index=False)
    print(data)
    print("deposite sucessfull")


def withdraw(data):
    ano=int(input("enter account no:"))
    query=data[data['account']==ano]
    draw=int(input("enter withdraw amount:"))
    if query.loc[0,['balance']][0]<draw:

         print("not enough amount")
         return

    reqindex=query.index[0]
    print(reqindex)
    data.loc[reqindex,['balance']]-=draw
    print(data)
    print("withdraw sucessfull:")


while(True):
    print("0-exit\n,1-create account\n,2-deposite\n,3-withdraw\n")
    n=int(input("enter the number:"))
    if n==0:
        data.to_csv("E:\python program\ bankdetail.csv", index=False)
        break
    if n==1:
        data=newac(data)
    if n==2:
        deposite(data)
    if n==3:
        withdraw(data)