# The numpy module gives users access to numpy arrays and several computation tools.
# Numpy arrays are list-like objects intended for computational use.

from pprint import pprint

import numpy as np

my_array = np.array([1, 2, 3])
pprint(my_array)


# Operations on a numpy array are made element by element (unlike for lists of numbers):
pprint(my_array+1), pprint(my_array*2), pprint(np.sin(my_array))


# Numpy arrays are equipped with several useful methods such as:
my_array.shape, my_array.min(), my_array.max()
print(my_array.shape, my_array.min(), my_array.max())


# The numpy module also features some convenient array-generating functions:
# Linear space of 20 pts between 0 and 10
my_array2 = np.linspace(0, 10, 20)
pprint(my_array2)

# Sequence of numbers from 0 to 10 with step of 0.2,
#   similar to range() but accepts non-integer steps
my_array3 = np.arange(0, 10, 0.2)
pprint(my_array3)


# Multi-dimensional arrays are created using nested list and a call to np.array()
# Here is an example of a 2D array:
my_array4 = np.array([[1, 2, 3], [4, 5, 6]])
pprint(my_array4)

# Items in a multi-dimensional array can be retrieved, like in a nested list, as:
my_array4[1][1]
print(my_array4[1][1])

# or

my_array4[0,2]
print(my_array4[0, 2])

# Moreover, numpy is equipped with several NaN (Not-a-Number) functions.
my_array5 = np.array([[1, np.nan], [np.nan, 2]])
pprint(my_array5)

np.nanmin(my_array5), np.nanmax(my_array5)
print(np.nanmin(my_array5), np.nanmax(my_array5))

np.isnan(my_array5)
pprint(np.isnan(my_array5))


# Finally, to concatenate numpy arrays, use:
np.concatenate([my_array,my_array2[0:5]])
pprint(np.concatenate([my_array,my_array2[0:5]]))







