def classify(features_train, labels_train):
    ### your code goes here--should return a trained decision tree classifer
    # Get decision tree classifier
    from sklearn import tree
    clf = tree.DecisionTreeClassifier(min_samples_split=50)

    # fit classifier to the features (usually the 'x') and the labels ('usually 'Y')
    clf.fit(features_train, labels_train)

    return clf