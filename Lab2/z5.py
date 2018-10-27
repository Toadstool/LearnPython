import numpy as np

#A=np.array([[1,2,3,4],[5,6,7,8],[7,8,9,11],[2,3,6,4]])
A = np.random.rand(100,100)
print(A)
b=np.array(range(1,101))
print(b)
x=np.linalg.solve(A,b)
print(x)

(A,b)
print(x)


