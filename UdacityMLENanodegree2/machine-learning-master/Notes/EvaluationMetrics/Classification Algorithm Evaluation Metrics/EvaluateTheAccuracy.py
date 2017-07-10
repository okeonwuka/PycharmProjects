# =====================================================================================================================
# In this and the following exercises, you'll be adding train test splits to the data
# to see how it changes the performance of each classifier
#
# The code provided will load the Titanic dataset like you did in project 0, then train
# a decision tree (the method you used in your project) and a Bayesian classifier (as
# discussed in the introduction videos). You don't need to worry about how these work for
# now.
#
# What you do need to do is import a train/test split, train the classifiers on the
# training data, and store the resulting accuracy scores in the dictionary provided.
# =====================================================================================================================

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
# the rest of the#Solution data.
y = X['Survived']


# Remove labels from the inputs, and age due to missing data (data cleansing)
del X['Age'], X['Survived']


# Import classifiers used in this experiment
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB


# split the data into training and testing sets,
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

# Get the decision tree accuracy score, dt_score, by applying the accuracy function on the 'test set' data of features and labels ie features_test & labels_test
dt_score = accuracy_score(labels_test, clf1.predict(features_test))
print "Decision Tree has accuracy: ", dt_score



# The naive Bayes classifier
# clf2 = GaussianNB()
# clf2.fit(features,labels)

# First, as usual create the classifier, clf2
clf2 = GaussianNB()

# Train the Gaussian naive bayes classifier with labels_train and features_train
clf2.fit(features_train, labels_train)

# Get the Gaussian naive bayes accuracy score, nb_score, by applying the accuracy function on the 'test set' data of features and labels ie features_test & labels_test
nb_score = accuracy_score(labels_test, clf2.predict(features_test))
print "GaussianNB has accuracy: ", nb_score


answer = {
 "Naive Bayes Score": dt_score,
 "Decision Tree Score": nb_score
}

print answer

