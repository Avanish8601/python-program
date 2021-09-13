n=72
flag=1  #when flag=1 not prime
if n==1:
    print("not prime")

for i in range(2,int(n**(1/2)+1)):
    if n%i==0:
        flag=0
        break
if flag==1:
    print(n,"is prime no")
else:
    print(n,"is not prime no ")

