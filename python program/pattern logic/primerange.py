s=int(input("enter first element:"))
l=int(input("enter last element:"))
for i in range(s,l):
    flag=1
    for j in range(2,int(i**(1/2)+1)):
        if i%j==0:
            flag=0
    if flag==1:
        print(i,end=" ,")

