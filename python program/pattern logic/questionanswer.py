"""a="sachin RamESh TEnDulKar"
a=a.title()
print(a)
                         #output= Sachin Ramesh Tendulkar
a=a.upper()
print(a)
a=a.lower()
print(a)"""

#########prime numbers between 1-100##########

"""for i in range(1,100):
    n=i
    flag=0
    if n==0 or n==1:
        flag=1
    for i in range(2,int (n**(1/2)+1)):
        if n%i==0:
            flag=1
    if flag==0:

        print(n,"prime no")
    else:
        print(n ,"not prime no")"""


######## Proper case of words###################
"""a= 'sachin rAMesH TenDULkar'
b=""
for i in range(len(a)):
    if i==0:
        b+=a[i].upper()
    elif ord(a[i-1])==32:
        b+=a[i].upper()
    else:
        b+=a[i].lower()
print(b)"""
###########list , find sublist############## output=[3,4,6,8]

"""l=[2,4,9,1,4,5,3,4,6,8,0,1]
l=l[6:10]
print(l)
"""
## question -9 removes all repeated words in given words ################

"""a= "varanasi"
b=""
for i  in range(len(a)):
    if a[i] in b:
        pass
    else:
        b=b+a[i]
print(b)"""
 ###### find all words starting with a vowel###########

"""def Vowel(v):
    v=v.lower()
    if v=="a" or v=="e" or v=="i" or v=="o" or v=="u":
        return True
    return False
s="this is an elephant"
for i in range(len(s)):
    if s[i]==0 or s[i-1]==' ':

        if Vowel(s[i]):
            while(i<len(s) and s[i]!=' ' ):
                print(s[i],end="")
                i+=1
            print(" ",end="")"""


############# largest sequencing element in list ############

"""l=[2,5,9,1,4,5,3,4,6,8,0,1]
n=len(l)
l=l+[l[n-1]-1]
print(l)
n=n+1
maxlen=-1
maxseq=0
currentseq=[]
for i in range(1,n):
    prev=l[i-1]
    current=[l[0]]
    if current >prev:
        currentseq=currentseq+[current]
    else:
        if(len(currentseq))>maxlen:
            maxlen=len(currentseq)
            maxseq=current.copy()
            currentseq=[current]
print(maxseq)"""

###########permputation of words kashi
l=[0,0,0]
n=len(l)
for i in range(n):
    print(l[i],end=" ")
for i in range(2**n):
    print(l)
    for j in range(n-1,-1,-1):
        if l[j]==0:
            l[j]=1
            break
        l[j]=0
s="abc"
count=0
for i in range(3):
    for j in range(3):
        if i==j:
            continue
        for k in range(3):
            if i==k or j==k:
                continue

            print(s[i],s[j],s[k])
            count+=1
print(count)



