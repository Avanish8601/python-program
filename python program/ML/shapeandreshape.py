import numpy
from sklearn.metrics import r2_score
x=[1,2,3,4,5,6]
x=numpy.array(x)
print(x.shape)
print(x.reshape(2,-1))
print(x.reshape(2,2,-1))
print(x*x)

