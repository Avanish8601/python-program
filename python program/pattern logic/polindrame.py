"""n=int(input("enter the no:"))
temp=n
rev=0
while(n>=1):
    digit=n%10
    rev=rev*10+digit
    n=n//10
if temp==rev:
    print(n,"is palindrome")
else:
    print(n,"is not polindrame")
"""

n='123'
flag=1
i=0
j=len(n)-1
for i in range(len(n)):
    for j in range(len(n)-1,-1,-1):
        if n[i]==n[j]:
            flag=0
            break
if flag==1:
    print(n,"is palindrome")
else:
    print(n,"is not palindrome")


