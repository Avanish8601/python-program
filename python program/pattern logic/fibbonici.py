"""def fabb(n):
    a=0
    b=1
    if n<0:
        print("wrong input")
    elif n==0:
        return a
    elif n==1:
        return b
    else:
        for i in range(1,n+1):
            c=a+b
            a=b
            b=c
        return c
n=10
print(fabb(n))
"""




###### perfect cube#######
"""n=int(input("enter the no:"))
cube=0
for i in range(n+1):
    cube=i*i*i

if cube==n:
    print(n,"is a perfect cube")
elif cube>n:
    print(n,"is not perfect cube")"""

######### digit convert in alphabet#######

def printvalue(n):
    if n==0:
        print("zero")
    elif n==1 :
        print("one",)
    elif n==2:
        print("two")
    elif n==3:
        print("three")
    elif n==4:
        print("four")
    elif n==5:
        print("five")
    elif n==6:
        print("six")
    elif n==7:
        print("seven")
    elif n==8:
        print("eight")
    elif n==9:
        print("nine")
def printword(n):
    i=0
    lenth=lin(n)
    while i<lenth:
        printvalue(n[i])
        i+=1
n=123
printword(n)+




