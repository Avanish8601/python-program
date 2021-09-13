"""#swaping to variable
x=5
y=7
x,y=y,x
print("value x after swaping=",x)
print("value y after swaping=",y)"""

#pattern
"""n=7
for i in range(n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,i):
        print(k,end="")
    for k in reversed(range(1,i-1)):
        print(k,end="")
    print("")
"""

#find difference largest and smallest element in list
"""l=[4,6,3,7,9,11]
print("max element=",max(l))
print("min element=",min(l))
difference=max(l)-min(l)
print(difference) """

#reverse of digit numbers
"""n=123
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("rev=",rev)"""

#sum of digit
"""s=1
l=100
sum=0
for i in range(s,l+1):
    sum=sum+i
print(sum,end="")
"""
#polindrame number

"""n=int(input(""))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if (temp==rev):
    print("number is polindrome")
else:
    print("number is not polindrome")
"""

#count the number of digits

"""n=12345
count=0
while(n>0):
    count=count+1
    n=n//10
print("digit=",count)"""

