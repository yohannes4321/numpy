#!/usr/bin/python3
import numpy as np
d=np.ones((3,4))
t=np.arange(2,5,2)
print(t)
# in numpy file np.arange 
print(np.linspace(2,5,2))
o=np.array([[1,2,3],[4,5,6]])
print(o.shape)
print(o.reshape(3,2))
print(o.ravel())
# ravel is function and return new array with 1 dimsnsional it doesnot change the orginal array
print(o)
print("min {} max{}".format(o.min(),o.max()))
print(o.sum())
# axis =0 mean column wise and axis =1 mean row wise
print(o.sum(axis=0))
print(o.sum(axis=1)) 
print(np.sqrt(o))
# np for standard deviation
print(np.std(o))
s=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(o.dot(s))