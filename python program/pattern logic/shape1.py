n=7
for i in range(1,n+1):
    for j in range(1,n+1):
        condition= j==n or i==n or i+j==n+1
        if condition:
            print("*",end="")
        else:
            print(" ",end="")
    print()