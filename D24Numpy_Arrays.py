import numpy as np

'''
Arrays support vectorized operations, while lists dont.
Once an array is created, you cannot change its size. You will have to create a new array or overwrite the existing one.
Every array has one and only one dtype. All items in it should be of that dtype.
An equivalent numpy array occupies much less space than a python list of lists.
numpy arrays support boolean indexing.
'''

print(np.__version__) # check version
# print(dir(np)) checks all available methods
py_list = [[1, 3, 5], [2, 4, 6]] # regular list
py_tuple = (1, 2, 3) # regular tuple
# list to array, dtype could be str, int, bool, float, complex, None
numpy_arr = np.array(py_list, dtype=bool)
numpy_arr2 = np.array(py_tuple, dtype=float)
print(numpy_arr)
print(numpy_arr2, type(numpy_arr2))
# converts back to list
numpy_arr2 = numpy_arr2.tolist() 
print(numpy_arr2, type(numpy_arr2))
# shape of array
print(numpy_arr.shape)
# size of array
print("HIIIIIIIIIIIIIIIIIIIIIIIIII")
print(numpy_arr.size)
print(numpy_arr.itemsize)
# dtype of array
print(numpy_arr.dtype)
# array math - applies to all elements at once
numpy_arr3 = np.array([1, 2, 3, 4, 5])
numpy_arr3[0] = 100
numpy_arr3 *= 3
numpy_arr3 = np.array(numpy_arr3, dtype=float)
print(numpy_arr3)
# indexing arrays
numpy_arr4 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(numpy_arr4[0][0]) # row 1 item 1
print(numpy_arr4[:-1, 0:2]) # all but last row, first two items in each row
print(numpy_arr4[::-1, ::-1]) # reversed rows reversed items
# shape changing
numpy_arr5 = np.ones((3, 3), dtype=int) # make 3x3 array with 1s
numpy_arr5 = numpy_arr5.reshape(9, 1) # reshape to 9x1
print(numpy_arr5.flatten()) # flattens to one row (now 1x9)
# combining arrays
arr1, arr2 = [1,2,3], [4,5,6]
print(np.hstack((arr1, arr2))) # horizontally appending (all nums in one row)
print(np.vstack((arr1, arr2))) # vertically appending (two rows in one array)
# random stuff
rand_arr = np.random.random(5) # array with 5 random elements
rand_arr2 = np.random.randint(1, 4, size=(2, 5)) # array with 2 rows 5 random elements from 1-3
rand_arr3 = np.random.choice([1, 2, 3, 4, 5], size=3)
rand_arr4 = np.random.rand(3, 3) # same as random but can choose dimensions
print(rand_arr)
print(rand_arr2)
print(rand_arr3)
print(rand_arr4)