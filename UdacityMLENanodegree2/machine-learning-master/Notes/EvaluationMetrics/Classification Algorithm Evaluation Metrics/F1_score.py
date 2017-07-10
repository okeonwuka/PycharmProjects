# As usual, use a train/test split to get a reliable F1 score from two classifiers, and
# save it the scores in the provided dictionaries.


# Import library's needed
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


# Import classifiers and evaluation metric used in this experiment
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score
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

# Get the decision tree F1_score dt_F1_score, by applying the f1_score function on the 'test set' data of features and labels ie features_test & labels_test
dt_F1_score = f1_score(labels_test, clf1.predict(features_test))
print "Decision Tree F1 score: {:.2f}".format(f1_score(labels_test, clf1.predict(features_test)))

# The naive Bayes classifier
# clf2 = GaussianNB()
# clf2.fit(features,labels)

# First, as usual create the classifier, clf2
clf2 = GaussianNB()

# Train the Gaussian naive bayes classifier with labels_train and features_train
clf2.fit(features_train, labels_train)

# Get the naive bayes F1_score, nb_F1_score, by applying the f1_score function on the 'test set' data of features and labels ie features_test & labels_test
nb_F1_score = f1_score(labels_test, clf2.predict(features_test))
print "GaussianNB F1 score: {:.2f}".format(f1_score(labels_test, clf2.predict(features_test)))

F1_scores = {
 "Naive Bayes": nb_F1_score,
 "Decision Tree": dt_F1_score
}
print F1_scores
