n=7
for i in range(1,n+1):
    for j in range(1,n+1):
        condition= i==j or i+j==n+1 or i==1 or j==1 or i==n or j==n
        if condition:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()