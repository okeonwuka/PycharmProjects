# Impoer necessary library
import numpy as np

# Create an list.  Numpy will cast this list as a 'numpy array' behind the scenes
numbers = [1,2,3,4,5]

#  find mean
numbers_mean = np.mean(numbers)
print numbers_mean

#  find median
numbers_median = np.median(numbers)
print numbers_median

# find standard deviation
numbers_standarddeviation = np.std(numbers)
print numbers_standarddeviation
print '=========================================1=========================================================='

# Numpy is battle tested and optimized so that it runs fast, much faster than if you were working with Python lists directly
array = np.array([1, 4, 5, 8], float)
print array
print ""

# a 2D array/Matrix
array = np.array([[1, 2, 3], [4, 5, 6]], float)
print array
print '=========================================2=========================================================='

# You can index, slice, and manipulate a Numpy array much like you would with a  Python list.
array = np.array([1, 4, 5, 8], float)
print array
print array[1]
print array[:2]
array[1] = 5.0
print array[1]
print '=========================================3=========================================================='

# Matrix indexing and slicing
# the indexing starts at 0 not 1.  General format  = array_name[(n-1) array/row ][(n-1) element in array/row.....not column]
two_D_array = np.array([[1, 2, 3], [4, 5, 6]], float)
print two_D_array
print ""
print two_D_array[1][1]
print two_D_array[0][0]
print two_D_array[0][1]
print two_D_array[0][2]
print two_D_array[1][1]
print two_D_array[1][2]

print '==================================================================================================='
three_D_array = np.array([[1, 2, 3], [4, 5, 6],[7, 8, 9]], float)
print three_D_array
print three_D_array[2][2]
print three_D_array[2]
print three_D_array[2][0]
print three_D_array[2][1]

print '=========================================4=========================================================='

#  print  entire rows. result is 1 x n array
print two_D_array[0, :]
print two_D_array[1, :]

# print entire columns. result is n x 1 array
print two_D_array[:, 0]
print two_D_array[:, 1]
print three_D_array[:, 2]

print '=========================================5=========================================================='

# array multiplication
# note addition and subtraction operations are similar to multiplication
array_1 = np.array([1, 2, 3], float)
array_2 = np.array([5, 2, 6], float)
print array_1 * array_2


print '=========================================6=========================================================='

# More examples
array_1 = np.array([[1, 2], [3, 4]], float)
array_2 = np.array([[5, 6], [7, 8]], float)
print array_1 * array_2
print '===================================================================================================='
print array_1 + array_2
print '=========================================7=========================================================='

# other numpy mathematical operations on Numpy arrays
array_1 = np.array([1, 2, 3], float)
array_2 = np.array([[6], [7], [8]], float)
print np.mean(array_1)
print np.mean(array_2)
print np.dot(array_1, array_2)











