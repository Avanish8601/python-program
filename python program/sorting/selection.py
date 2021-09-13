l=[4,6,2,7,1,9]
for i in range(len(l)-1):
    min=l[i]
    minpos=i
    for j in range(i+1,len(l)):
        if min>l[j]:
            min= l[j]
            minpos=j
            l[i],l[minpos]=l[minpos],l[i]
print(l,end=",")