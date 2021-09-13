"""def decimal(n):
    binarynum=0
    i=0
    while(num>=1):
        rem=num%2
        binarynum=binarynum+rem*(10**i)
        num=num//2
        i=i+1
    print("binary no=",binarynum)
num=16
decimal(num)"""

num=int(input("enter the no:"))
binarynum = 0
i = 0
while (num >=1):
    rem = num % 2
    binarynum = binarynum + rem * (10 ** i)
    num = num // 2
    i = i + 1
print("binary no=", binarynum)

"""def decimal(num):
    if num>=1:
        decimal(num//2)
    print(num%2)
num=7
decimal(num)"""