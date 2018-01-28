import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()

##################################################################################


########################## DECISION TREE #################################
from sklearn import tree

clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)

#### your code goes here
# Import accuracy_score
from sklearn.metrics import accuracy_score

# Get the prediction y_pred
# Get the prediction y_pred (Prediction done on features of the test data...features_test.
# We are predicting what label the algorithm will give to the data feature)
y_pred = clf.predict(features_test)

### you fill this in!
### be sure to compute the accuracy on the test set
# After predicting the features to generate the predicted label, y_pred, We test the accuracy of this
# label by comparing it to the corresponding correct labeling of the test data set (ie the corresponding
# labels ie label_test for the features_test.
acc = accuracy_score(labels_test, y_pred)


def submitAccuracies():
    return {"acc": round(acc, 3)}