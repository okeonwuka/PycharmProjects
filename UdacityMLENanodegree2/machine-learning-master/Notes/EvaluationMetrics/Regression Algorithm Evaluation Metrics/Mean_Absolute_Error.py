# Import necessary library
import numpy as np
import pandas as pd

# Load the dataset
from sklearn.datasets import load_linnerud

linnerud_data = load_linnerud()
X = linnerud_data.data
y = linnerud_data.target

from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error as mae
from sklearn.linear_model import LinearRegression

# TODO: split the data into training and testing sets,
# using the standard settings for train_test_split.
# Then, train and test the classifiers with your newly split data instead of X and y.

#Solution
# Prepare the data as features and labels.
features = X
labels = y

# split the data into training and testing sets
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.4, random_state=0)

# Create decision tree regressor/algorithm object
reg1 = DecisionTreeRegressor()

# Train the decision tree regressor using the 'trains' ie features_train, labels_train
reg1.fit(features_train, labels_train)

# Get the decision tree regressor Mean Absolute Error, dtr_mae, using the 'tests' ie labels_test and features_test
dtr_mae = mae(labels_test, reg1.predict(features_test))

print "Decision Tree mean absolute error: {:.2f}".format(mae(labels_test, reg1.predict(features_test)))


# Create the linear Regression regressor/algorithm object
reg2 = LinearRegression()

# Train the linear Regression regressor using the 'trains' ie features_train, labels_train
reg2.fit(features_train,labels_train)

# Get the linear Regression regressor Mean Absolute Error, lr_mae, using the 'tests' ie labels_test and features_test
lr_mae = mae(labels_test, reg2.predict(features_test))

print "Linear regression mean absolute error: {:.2f}".format(mae(labels_test, reg2.predict(features_test)))

results = {
 "Linear Regression": lr_mae,
 "Decision Tree": dtr_mae
}                                                                                                                                                                                                              

print results
