# As with other classifiers, DecisionTreeClassifier takes as input two arrays: an array X, sparse or dense,
# of size [n_samples, n_features] holding the training samples, and an array Y of integer values, size [n_samples],
# holding the class labels for the training samples

from sklearn import tree
X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

# After being fitted, the model can then be used to predict the class of samples:
a = clf.predict([[2., 2.]])



# Using the Iris dataset, we can construct a tree as follows
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)


