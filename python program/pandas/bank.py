import pandas as pd
data=pd.read_csv("bank1.csv")
data['status']='open'
def checkaccno(data,accno):
    t=False
    if accno in list(data['accno']):
        t=True
    return t
def deposite(data):
    ano=int(input("enter account no:"))
    query=data[data['accno']==ano]
    dep=int(input("enter amount:"))
    reqindex=query.index[0]
    data.loc[reqindex,['balance']] += dep
    #data.to_csv("bank1.csv",index=False)
    print(data)
    print("deposite sucessfull")


def withdraw(data):

    ano=int(input("enter account no:"))
    query=data[data['accno']==ano]
    draw=int(input("enter withdraw amount:"))
    if query.loc[0,['balance']][0]<draw:

         print("not enough amount")
         return

    reqindex=query.index[0]
    print(reqindex)  
    data.loc[reqindex,['balance']]-=draw
    print(data)
    print("withdraw sucessfull:")


def newac(data):
    name=input("enter name:")
    newac=int(input("enter new account no:"))
    if checkaccno(data,newac):

        print("accoun'/t number already exist")

        return data

    bal=int(input("enter opening balance ammount:"))
    new={'name':name,'accno':newac,'balance':bal,'status':open}
    data=data.append(new, ignore_index= True)
    print(data)
    print("account create sucessfull:")
    return data
def balanceinq(data):
    acno=int(input("enter the account no for balance enquary:"))
    query=data[data['accno']==acno]
    index=query.index[0]
    bal=query.loc[index,['balance']][0]
    print(" available balance=",bal)
def delaccno(data):
    accno=int(input("enter the account no for closed:"))
    query=data[data['accno']==accno]
    index=query.index[0]
    data.loc[index,['status']]='closed'
    print("account closed sucessfull")




while(True):
    print("0-exit\n,1-deposite\n,2-withdraw\n,3-open new account\n,4-balance inquary\n,5-closed account")
    n = int(input("enter the no:"))
    if n==0:
        data.to_csv("E:\python program\ bank1.csv",index=False)
        break
    if n==1:
        deposite(data)
    if n==2:
        withdraw(data)
    if n==3:
        data=newac(data)
    if n==4:
        balanceinq(data)
    if n==5:
        delaccno(data)


