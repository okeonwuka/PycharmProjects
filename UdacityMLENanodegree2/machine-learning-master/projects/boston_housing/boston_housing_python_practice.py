# Hey....i just noticed that the libraries that are imported remain greyed out until you use it. Nice!
# Import libraries necessary for this project
import numpy as np
import pandas as pd
from sklearn.cross_validation import ShuffleSplit

# ------ Only needed for jupyter notebook -----------------
# Import supplementary visualizations code visuals.py
# import visuals as vs
# Pretty display for notebooks
# %matplotlib inline
# ------------------------------------------------------------


# Load the Boston housing dataset
data = pd.read_csv('housing.csv')
prices = data['MEDV']
features = data.drop('MEDV', axis = 1)

# Success
print "Boston housing dataset has {} data points with {} variables each.".format(*data.shape)
print data, prices,features


# ======================================Data Exploration=====================================
print '======================================Data Exploration====================================='
# Mean price of the data
mean_price = np.mean(prices)
print '1. Mean price of the data is ${:,.2f}'.format(mean_price)

# Median price of the data
median_price = np.median(prices)
print '2. Median price of the data is ${:,.2f}'.format(median_price)

# Maximum price of the data
maximum_price =np.max(prices)
print '3. Maximum price of the data is ${:,.2f}'.format(maximum_price)

# Minimum price of the data
minimum_price = np.min(prices)
print '4. Minimum price of the data is ${:,.2f}'.format(minimum_price)

# Standard deviation of prices of the data
std_price = np.std(prices)
print '5. standard dev of price of the data is ${:,.2f}'.format(std_price)
print ''

print '=================================Developing a Model ================================'

# Define R2 performance metric

from sklearn.metrics import r2_score

def performance_metric(y_true, y_predict):
    """ Calculates and returns the performance score between
        true and predicted values based on the metric chosen. """

    # Calculate the performance score between 'y_true' and 'y_predict'
    score = r2_score(y_true, y_predict)

    # Return the score
    return score

# Test
# y_t = [2.5, -0.5, 2, 8]
# y_p = [2.5, 0.0, 2, 8]
# print performance_metric(y_t,y_p)

print ''

print '=================================Implementation: Shuffle and Split Data ================================'
