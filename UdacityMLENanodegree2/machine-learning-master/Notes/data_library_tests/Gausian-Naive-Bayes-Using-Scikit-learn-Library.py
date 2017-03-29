import numpy as np

# Training data
# X represents the features
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])

# Y represents the labels
Y = np.array([1, 1, 1, 2, 2, 2])

print X, Y

# Import GaussianNB algorithm
from sklearn.naive_bayes import GaussianNB

# Create a classifier
clf = GaussianNB()

# Fit/train the training data to learn the patterns
clf.fit(X, Y)
GaussianNB()
# Test classifier 'clf' that has just been created by giving it new points to make predictions on
print(clf.predict([[-0.8, -1]]))

