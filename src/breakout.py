import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

eculidian = []
for i in range(len(a)):
    euclidian += ( (a[i] -b[i]) ** 2)
result = sum(euclidian)

list = (a -b)**2
list