def studentReg(ages_train, net_worths_train):
    ### import the sklearn regression module, create, and train your regression
    from sklearn import linear_model

    ### name your regression reg (create your regression model/algorithm. If this was a classification task and not regression we'd call this creating a classifier)
    reg = linear_model.LinearRegression()

    ### your code goes here! (fit your regression model to the data you trained?)
    reg.fit(ages_train, net_worths_train)


    return reg
