n=7
for i in range(1,n+1):
    for j in range(1,n-i+11):
        print(" ",end="")
    for k in range(1,i):
        print("*",end="")
        print(" ",end="")
    print()