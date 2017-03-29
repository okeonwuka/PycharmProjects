# While you Manipulate data in numpy you store and reference it using pandas.
# For this use the "Dataframe" structure in pandas.  Its just a table
# In general, create a dictionary and pass it as an argument to the dataframe function to create a dataframe
# a Series as an one-dimensional object that is similar to an array, list, or column in a database. By default, it will assign an
# index label to each item in the Series ranging from 0 to N, where N is the number of items in the Series minus one.

import pandas as pd


print '======================================1======================================='
series = pd.Series(['Dave', 'Cheng-Han', 'Udacity', 42, -1789710578])
print series


# You can also manually assign indices to the items in the Series when creating the series. Just add an index array
print '======================================2======================================='
series = pd.Series(['Dave', 'Cheng-Han', 359, 9001], index=['Instructor', 'Curriculum Manager', 'Course Number', 'Power Level'])
print series


# You can use index to select specific items from the Series
print '======================================3======================================='
print series['Instructor']
print '======================================4======================================='
print series[['Instructor', 'Curriculum Manager', 'Course Number']]


# You can also use boolean operators to select specific items from the Series
print '======================================5======================================='
cuteness = pd.Series([1, 2, 3, 4, 5], index=['Cockroach', 'Fish', 'Mini Pig', 'Puppy', 'Kitten'])
print cuteness
print '======================================6======================================='
print cuteness > 3
print '======================================7======================================='
print cuteness[cuteness > 3]
