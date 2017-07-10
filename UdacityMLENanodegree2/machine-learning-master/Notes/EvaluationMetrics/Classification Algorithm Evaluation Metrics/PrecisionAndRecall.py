# As with the previous exercises, let's look at the performance of a couple of classifiers
# on the familiar Titanic dataset. Add a train/test split, then store the results in the
# dictionary provided.

import numpy as np
import pandas as pd

# Load the dataset
X = pd.read_csv('titanic_data.csv')

# Limit to numeric data
X = X._get_numeric_data()


# Separate the labels. (the nature of the problem is to train the algorithm to predict
# who did and did not survive based on the data given. Since the answer/actual result
# of who did and did not survive is with the data given, We need to separate this from
# the rest of the data.
y = X['Survived']


# Remove labels from the inputs, and age due to missing data (data cleansing)
del X['Age'], X['Survived']

# Import classifiers and evaluation metric to be used in this experiment
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import recall_score as recall
from sklearn.metrics import precision_score as precision
from sklearn.naive_bayes import GaussianNB

# TODO: split the data into training and testing sets,
# using the standard settings for train_test_split.
# Then, train and test the classifiers with your newly split data instead of X and y.

# Solution:
# Prepare the data as features and labels. Based on the above arrangement, y = X['Survived'] will be the label
# while X will be the features....in this case because of the data cleansing above its all non-Nan, numeric data

features = X
labels = y

from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.4, random_state=0)

# The decision tree classifier
# clf1 = DecisionTreeClassifier()
# clf1.fit(features,labels)

# create the decision tree classifier, clf1
clf1 = DecisionTreeClassifier()

# Train the decision tree classifier with labels_train and features_train ( you 'train' with the 'trains')
clf1.fit(features_train, labels_train)

#Use precision and recall evaluation metric to test the 'test' data  ie features_test and label_test
print "Decision Tree recall: {:.2f} and precision: {:.2f}".format(recall(labels_test, clf1.predict(features_test)), precision(labels_test, clf1.predict(features_test)))

# As seen in above line
# Get the decision tree recall 'dt_recall by applying recall function on 'test set' data of features and labels ie features_test & labels_test
dt_recall = recall(labels_test, clf1.predict(features_test))

# Also
# Get the decision tree precision 'dt_precision by applying precision function on 'test set' data of features and labels ie features_test & labels_test
dt_precision = precision(labels_test, clf1.predict(features_test))




# The naive Bayes classifier
# clf2 = GaussianNB()
# clf2.fit(features,labels)

# First, as usual create the classifier, clf2
clf2 = GaussianNB()

# Train the Gaussian naive bayes classifier with labels_train and features_train
clf2.fit(features_train, labels_train)

#Use precision and recall evaluation metric to test the 'test' data  ie features_test and label_test
print "GaussianNB recall: {:.2f} and precision: {:.2f}".format(recall(labels_test,clf2.predict(features_test)), precision(labels_test,clf2.predict(features_test)))

# As seen in above line
# Get the naive bayes recall 'nb_recall by applying recall function on 'test set' data of features and labels ie features_test & labels_test
nb_recall = recall(labels_test, clf2.predict(features_test))

# Also
# Get the naive bayes precision 'nb_precision by applying precision function on 'test set' data of features and labels ie features_test & labels_test
nb_precision = precision(labels_test, clf2.predict(features_test))


results = {
  "Naive Bayes Recall": nb_recall,
  "Naive Bayes Precision": nb_precision,
  "Decision Tree Recall": dt_recall,
  "Decision Tree Precision": dt_precision
}

print results
