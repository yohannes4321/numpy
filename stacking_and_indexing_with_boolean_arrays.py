#!/usr/bin/python3
import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
print(a[0:1])
c=np.array([[2,3,4],[5,6,7]])
print(c[1,2])
print(c[-1,-1])
print(c[0:2,0:2])
print(c[:,1:])
# iterate over the array
for row in c:
    print(row)
print("----------------")
for row in c.flat:
    print(row)
# stacking arrays
j=np.array([[1,2,3],[4,5,6]])
jd=np.array([[7,8,9],[10,11,12]])
print(np.vstack((j,jd)))
#to stack and to connect vertically
print(np.hstack((j,jd)))
#to stack and to connect horizontally
# splitting arrays
print("----------------")
print(np.vsplit(c,2))
print(np.split(c,2))
# indexing with boolean arrays
j=np.arange(12).reshape(3,4)
bb=j>4
print(bb)
#  p rint array inside array
j[bb]=-1
print(j[bb])









