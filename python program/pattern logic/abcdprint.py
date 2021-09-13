n=5
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,i+1):
        x=ord("A")
        ch=chr(x+k-1)
        print(ch,end="")
    for k in reversed(range(1,i)):
        x = ord("A")
        ch = chr(x + k - 1)
        print(ch,end="")
    print()