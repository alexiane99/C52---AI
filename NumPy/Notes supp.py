import numpy as np 

# VECTORIZATION 


a1 = np.array([2, 4, 6, 8, 10])
num = 2
res = a1 + num
print(res)
# [ 4  6  8 10 12]


a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
res = a1 + a2
print(res)
# [5 7 9]

a1 = np.array([10, 20, 30])
res = a1 > 15
print(res)
# [False  True  True]