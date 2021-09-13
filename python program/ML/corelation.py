import matplotlib.pyplot as plt
def corelation(px,py):
    n=len(px)
    sumx=0
    sumy=0
    sumXY=0
    sumX2=0
    sumY2=0
    for i in range (n):
        x = px[i]
        y = py[i]
        sumx += x
        sumy += y
    meanx=sumx/n
    meany=sumy/n

    for i in range(n):
         X=px[i]-meanx
         Y=py[i]-meany

         sumX2+= X*X
         sumY2+= Y*Y
         sumXY+= X*Y
    print(sumX2,sumY2,sumXY)
    r=(sumXY)/(sumX2*sumY2)**(1/2)
    return r
x=[105,104,102,101,100,99,98,96,93,92]
y=[101,103,100,98,95,96,104,92,97,94]
result=corelation(x,y)
print(result)
#plt.scatter(x,y,color='red',marker='o')
plt.bar(x,y,color='red')
plt.show()

