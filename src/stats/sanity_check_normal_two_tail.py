# sanity check calculations


import numpy as np


female=  62378
male=    37622
total_animals= female + male

females_arr = [1] * 5
females_arr
males_arr = [0] * 3
males_arr


females_arr.extend(males_arr)
sum(females_arr) #sanity check
males_arr.extend(females_arr)
sum(males_arr)

x = males_arr.extend(females_arr)

print("\nOriginal male array:")
print(x)
r1 = np.mean(x)
r2 = np.average(x)
assert np.allclose(r1, r2)
print("\nMean: ", r1)
r1 = np.std(x)
r2 = np.sqrt(np.mean((x - np.mean(x)) ** 2 ))
assert np.allclose(r1, r2)
print("\nstd: ", 1)
r1= np.var(x)
r2 = np.mean((x - np.mean(x)) ** 2 )
assert np.allclose(r1, r2)
print("\nvariance: ", r1)