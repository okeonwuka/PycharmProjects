# In this exercise, we'll use the Titanic dataset as before, train two classifiers and
# look at their confusion matrices. Your job is to create a train/test split in the data
# and report the results in the dictionary at the bottom.

import numpy as np
import pandas as pd

# Load the dataset
from sklearn import datasets

X = pd.read_csv('titanic_data.csv')
X = X._get_numeric_data() # X is the features

y = X['Survived'] #  y is the Predictions/ labels
del X['Age'], X['Survived'] # Get rid of incomplete data

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB

# split the data into training and testing sets
features = X
labels = y

from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.25, random_state=0)

# Create decision tree classifier
clf1 = DecisionTreeClassifier()
# Train decision tree classifier ('train' with the 'trains')
clf1.fit(features_train, labels_train)

# Create the gaussian naive bayes classifier
clf2 = GaussianNB()
# Train gaussian naive bayes classifier ('train' with the 'trains')
clf2.fit(features_train,labels_train)


# Prepare the confusion matrix for decision tree classifier
# for this, you use the '_test' data,e.g labels_test, features_test, because you want to test/evaluate
# the 'trained' data, using the confusion matrix evaluation metric to see how well the algorithm will perform
dt_confusion_matrix = confusion_matrix(labels_test, clf1.predict(features_test))
print "Confusion matrix for this Decision Tree:\n", dt_confusion_matrix

# Prepare the confusion matrix for gaussian naive bayes classifier
nb_confusion_matrix = confusion_matrix(labels_test, clf2.predict(features_test))
print "GaussianNB confusion matrix:\n", nb_confusion_matrix


# store the confusion matrices on the test sets below
confusions = {
 "Naive Bayes": nb_confusion_matrix,
 "Decision Tree": dt_confusion_matrix
}

print 'confusions =', confusions
