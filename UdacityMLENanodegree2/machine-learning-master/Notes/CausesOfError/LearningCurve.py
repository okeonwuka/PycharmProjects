# The Learning Curve functionality from sklearn let us learn about ways we can identify when our model performs well
#  It allows us to study the behavior of our model with respect to the number of data points being considered to
# understand if our model is performing well or not.

# From the documentation, a reasonable implementation of the function would be as follows:
# learning_curve( estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes)

# Where
#  estimator is the model which we are using to make our predictions with e.g GaussianNB()
# X and y are the features and label respectively
# cv is the cross validation generator, e.g KFold()
# n_jobs is the parameter that decides if we want to run multiple operations in parallel
# train_sizes is the number of training examples that will be considered to generate the curve



# Noisy data, Complex Model
# In this exercise we'll examine a learner which has high variance, and tries to learn
# nonexistant patterns in the data.
# Use the learning curve function from sklearn.learning_curve to plot learning curves
# of both training and testing error.


from sklearn.tree import DecisionTreeRegressor # Model we are using to make our predictions
import matplotlib.pyplot as plt
# PLEASE NOTE:
# In sklearn 0.18, the import would be from sklearn.model_selection import learning_curve
from sklearn.learning_curve import learning_curve # sklearn version 0.17
from sklearn.cross_validation import KFold # cross validation technique used is KFold
from sklearn.metrics import explained_variance_score, make_scorer
import numpy as np

# Set the learning curve parameters; you'll need this for learning_curves
size = 1000
cv = KFold(size,shuffle=True)
score = make_scorer(explained_variance_score)

# Create a series of data that forces a learner to have high variance (too much varying, overfitting)
# Notice the y is some sine curve......varying
X = np.round(np.reshape(np.random.normal(scale=5,size=2*size),(-1,2)),2)
y = np.array([[np.sin(x[0]+np.sin(x[1]))] for x in X])

def plot_curve():
    # Defining our regression algorithm
    reg = DecisionTreeRegressor()
    # Fit our model using X and y
    reg.fit(X, y)
    print "Regressor score: {:.4f}".format(reg.score(X,y))

    # TODO: Use learning_curve imported above to create learning curves for both the
    # training data and testing data. You'll need reg, X, y, cv and score from above.
    # Note: Because i didnt use all the parameters in order of function definition for learning_curve fn,
    #       I have to explicitly assign values to the parameters. e.g, from learning_curve fn, after 'y'
    #       comes 'train_sizes'. But since it is optional and I am not using that parameter, for all other parameters
    #       that come after, i have to explicitly assign values to the parameter (e.g cv=cv, scoring=score)
    #       else error
    train_sizes, train_scores, test_scores = learning_curve(reg, X, y, cv=cv, scoring=score)


    # Taking the mean of the test and training scores
    train_scores_mean = np.mean(train_scores,axis=1)
    test_scores_mean = np.mean(test_scores,axis=1)

    # Plotting the training curves and the testing curves using train_scores_mean and test_scores_mean
    plt.plot(train_sizes ,train_scores_mean,'-o',color='b',label="train_scores_mean")
    plt.plot(train_sizes,test_scores_mean ,'-o',color='r',label="test_scores_mean")

    # Plot aesthetics
    plt.ylim(-0.1, 1.1)
    plt.ylabel("Curve Score")
    plt.xlabel("Training Points")
    plt.legend(bbox_to_anchor=(1.1, 1.1))
    plt.show()

plot_curve()
