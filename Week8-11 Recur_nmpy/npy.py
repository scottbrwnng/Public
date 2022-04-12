from fileinput import filename
import numpy as np
import time as t
array0 = np.array([1,2,3,4])
array1 = np.genfromtxt('/Users/scott/Downloads/numpy_data.txt', np.dtype)

array2 = np.arange(6)

array3 = np.arange(2,51,2)

array4 = np.zeros((2,2))

array5 = np.ones((5,5))

array6 = np.eye(3)

array7 = np.diag([1,2,3,4,5,6,7,8,9,10])

array8 = np.full((13,13), 13)

array9 = np.random.random_integers(50,73,13)


a = np.array([1,2,3,4])
b = np.array([0,3,4,2])
c = b + 2
c = np.multiply(a,c)
print(c[2])

