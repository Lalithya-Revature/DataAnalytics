import numpy as np
arr=np.array([1,2,3])
print(arr)
print(type(arr))

a=np.zeros((2,3))
b=np.ones((3,2))
c=np.arange(0,10,2)
d=np.linspace(0,1,5)
e=np.random.rand(2,2)
print(a,b,c,d,e,sep='\n')

#one dimensional array
f=np.array([1,2,3])
g=np.array([4,5,6])
print(f+g)
print(f-g)
print(f**2)
print(np.sqrt(f))

#multi dimensional array
A = np.array([[1, 2], [3, 4]])
B = np.array([[1, 2], [3, 4]])
print(np.dot(A,B)) #Matrix mul
print(np.transpose(A)) # transpose
print(np.linalg.inv(A)) #inverse(if A is invertible)

arr=np.array([[10,20,30],[40,50,60]])
print(arr[0,1])
print(arr[:, 1])
print(arr[1])
   
   
####################
arr=np.array([1, 2, 3, 4])
print(arr.mean())
print(arr.sum())
print(arr.std())
print(arr.max())
print(arr.min())

