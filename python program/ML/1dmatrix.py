import numpy as np
import matplotlib.pyplot as plt
l=[[1,2,3],[4,5,6],[7,8,9]]
print(l)
new=[]
for i in range(len(l)):
    new=new+l[i]
print(new)

########multipliction of mtrix######
mat1=[1,2,3]
mat2=[4,5,6]
mat3=[]
for i in range(len(mat1)):
    for j in range(len(mat2)):
        mat3=mat1[i]*mat2[j]
        mat3=mat3.append(mat3)
    print(mat3)
