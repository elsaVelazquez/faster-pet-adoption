# add_column(np.array([[1, 2], [3, 4]]), np.array([5, 6)))
#     np.array([[1, 2, 5], [3, 4, 6]])
    
#     arr1 = np.array([[1, 2], [3, 4]]
                    
# arr2 = np.array([5, 6)))
    
# ret = np.array([[1, 2, 5], [3, 4, 6]])
import numpy as np
col = np.array([5, 6])
col_r= col.reshape(2,1)

arr = np.array([[1, 2], [3, 4]])
# ret = arr1 + new_col

# x = col
# y = 
# print(np.append(x, y, axis=1))


# import numpy as np
x = col_r
y = arr
# x = np.array([[10,20,30], [40,50,60]])
# y = np.array([[100], [200]])
print(np.append(col_r, arr, axis=1))



##### Q2
arr = np.array([[1, -1, 2], [3, 4, 2],[-8, 4, -4]])
def only_positive(arr):
    '''Return a numpy array containing only the rows from arr where all
    the values in that row are positive.
    USE NUMPY METHODS, AVOID USING A FOR-LOOP.

    Parameters
    ----------
    arr: NumPy Array (2-dimensional)

    Returns
    -------
    NumPy Array (2-dimensional)

    >>>np.array([[1, -1, 2],
                    [3, 4, 2],
                    [-8, 4, -4]])
    np.array([[3, 4, 2]])
    '''
arr = np.array([[1, -1, 2], [3, 4, 2],[-8, 4, -4]])
new_arr = (arr[arr> 0])
new_arr.reshape((3, 2))
new_arr.reshape(3, 3)

