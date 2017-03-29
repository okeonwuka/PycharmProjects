# Import necessary library
import numpy as np
import pandas as pd

# This code serves to play with dataframe concept in pandas
# Remember that the dataframe is like a table with rows and columns
# To create a dataframe, you can pass a dictionary of lists to the Dataframe constructor
# 1. The key of the dictionary is the column name
# 2. The associated list will be the values within that column.


# Dictionary of list looks like:
print '=================Dictionary of List ======================================='
data = {
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions','Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]
       }
print data
print '=================Dataframe construct ======================================='
football = pd.DataFrame(data)
print football
print ''

# Some Pandas functions: datatype,describe, head, tail
print '=================dtypes: to get the datatype for each column ======================================='
print football.dtypes
print '=================describe: useful for seeing basic statistics of the dataframes numerical columns =='
print football.describe()
print '=================head: displays the first five rows of the dataset ======================================='
print football.head()
print '=================head: displays the last five rows of the dataset ======================================='
print football.tail()
print ''


# Dataframe row selection methods: Slicing, and individual indexing (iloc or loc....where loc means 'locate'), Boolean indexing
print '=================iloc row selection method .... select row 0 ======================================='
print 'football.iloc[[0]]'
print football.iloc[[0]]
print '=================iloc row selection method .... select row 1 ======================================='
print 'football.iloc[[1]]'
print football.iloc[[1]]
print '=================loc row selection method .... select row 0 ========================================'
print 'football.loc[[0]]'
print football.loc[[0]]
print '==================================Slicing =========================================================='
print 'football[3:5]'
print football[3:5]
print '==================================Boolean Indexing=========================================================='
print 'football[football.wins > 10]'
print football[football.wins > 10]
print 'football[(football.wins > 10) & (football.team == "Packers")]'
print football[(football.wins > 10) & (football.team == "Packers")]
print ''


# Pandas vectorized methods
# This means to 'apply' a function to every single element in the dataframe...you can use the apply method
print '================= apply method ======================================='
data2 = {
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]
        }
print data2
print 'football2 = pd.DataFrame(data2)'
football2 = pd.DataFrame(data2)
print 'football2='
print football2

print 'use apply method'
print 'football2.apply(np.mean) = '
print football2.apply(np.mean)
print ''


# For operations cannot be vectorized like above ie take a numpy array as their input and return another array or value
# use 'map' for particular columns or 'applymap' for entire dataframes. These methods will take functions that enter a
# Single value and return a single value
# As a refresher on lambda, lambda functions are small inline functions that are defined on-the-fly in Python. lambda x: x>= 1
# will take an input x and return x>=1, or a boolean that equals True or False.
# In this example, map() and applymap() create a new Series or DataFrame by applying the lambda function to each element.
# Note that map() can only be used on a Series to return a new Series
# and applymap() can only be used on a DataFrame to return a new DataFrame.
print '================= map method: use for applying a function to 1 column in dataframe ======================================='
print 'football2[wins].map(lambda x: x >= 11) = '
print football2['wins'].map(lambda x: x >= 11)
print ''
print '================= applymap method: use for applying a function to ALL columns in dataframe ================================'
print 'football2.applymap(lambda x: x >= 11) = '
print football2.applymap(lambda x: x >= 11)
print ''










# Dataframe used in example:
print '==================================Dataframe used in example =========================================================='
countries = [
                'Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea',
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan'
             ]
gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

olympic_medal_counts = {'country_name': pd.Series(countries),
                                'gold': gold,
                              'silver': silver,
                              'bronze': bronze
                        }
df = pd.DataFrame(olympic_medal_counts)
print 'df = pd.DataFrame(olympic_medal_counts)'
print df
print ''

print '====== Digression: List Vs Series - list is horizontal while series is vertical, has indices & shows its datatype =========================================================='
print 'gold list'
print 'gold = '
print gold
print ''
print 'gold Series'
print 'pd.Series(gold) = '
print pd.Series(gold)
print ''
print ''
print 'countries list'
print 'countries = '
print countries
print ''
print 'countries Series'
print 'pd.Series(countries) = '
print pd.Series(countries)
print ''
print 'bronze at least one gold = '
print "df['bronze'][df['gold'] >= 1]"

print df['bronze'][df['gold'] >= 1]
print ''
print 'average bronze at least one gold ='
print "np.mean(df['bronze'][df['gold'] >= 1])"
print np.mean(df['bronze'][df['gold'] >= 1])
print ''

print 'average medal count = '
print "df[['gold', 'silver', 'bronze']].apply(np.mean)"
print df[['gold', 'silver', 'bronze']].apply(np.mean)
print ''

print '====== Numpy.dot  =========================================================='
print ''
print 'a = [a0,a1,a2,a3,a4]'
print 'b = [b0,b1,b2,b3,b4]'
print 'dot multiplication = a.b = (a0 x b0)+(a1 x b1)+(a2 x b2)+(a3 x b3)+(a4 x b4)'
print ''
print 'example'
a = [1, 2, 3, 4, 5]
print 'a = [1,2,3,4,5]'
b = [2, 3, 4, 5, 6]
print 'b = [2,3,4,5,6]'

print 'numpy.dot(a,b) = '
print np.dot(a, b)
print ''


print '====== Numpy matrix multiplication =========================================================='
print ''
print 'a = np.array([1, 2], float)'
a = np.array([1, 2], float)
print 'b = np.array([[2, 4, 6], [3, 5, 7]], float)'
b = np.array([[2, 4, 6], [3, 5, 7]], float)
print ''
print 'np.dot(a, b) = '
print np.dot(a, b)
print ''


print df

