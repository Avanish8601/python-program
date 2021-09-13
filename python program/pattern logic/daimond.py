n=7
mid=(n+1)/2
for i in range(1,n+1):
    for j in range(1,n+1):
        condition=i+j==mid+1 or i+j==mid+n or j-i==mid-1 or i-j==mid-1
        if condition:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
