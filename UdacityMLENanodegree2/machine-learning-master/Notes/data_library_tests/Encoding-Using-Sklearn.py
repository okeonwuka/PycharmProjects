import pandas
from sklearn import preprocessing

# create sample data
print 'create sample data (dictionary of lists):'
print 'sample_data = '
sample_data = {'name':   ['Ray', 'Adam', 'Jason', 'Varun', 'Xiao'],
               'health': ['fit', 'slim', 'obese', 'fit', 'slim']
              }
print sample_data
print ''


# storing sample data in the form of a dataframe
print 'storing sample data in the form of a dataframe:'
print "data = pandas.DataFrame(sample_data,columns = ['name', 'health']) ="
data = pandas.DataFrame(sample_data,columns = ['name', 'health'])
print data
print ''


# We have 3 different labels that we are looking to categorize: slim, fit, obese.
print 'We have 3 different labels that we are looking to categorize: slim, fit, obese.'
# To do this, we will call LabelEncoder() and fit it to the column we are looking to categorize.
print 'To do this, we will call LabelEncoder() and fit it to the column we are looking to categorize.'
label_encoder = preprocessing.LabelEncoder()
print 'label_encoder = preprocessing.LabelEncoder()'
print "label_encoder.fit(data['health'])"
label_encoder.fit(data['health'])
print ''


# Once you have fit the label encoder to the column you want to encode,
print 'Once you have fit the label encoder to the column you want to encode'
# you can then transform that column to integer data based on the categories found in that column.
print 'you can then transform that column to integer data based on the categories found in that column'
# That can be done as follows:
print 'That can be done as follows:'
print "label_encoder.transform(data['health']) ="
print label_encoder.transform(data['health'])
print ''


# You can combine the fit and transform statements above by using:
print 'You can combine the fit and transform statements above by using:'
print "label_encoder.fit_transform(data['health']) = "
print label_encoder.fit_transform(data['health'])
print ''

# The string categorical health data has been mapped as follows:
print 'The string categorical health data has been mapped as follows:'
print "label_encoder.fit_transform(data['health']) = "
print label_encoder.fit_transform(data['health'])

# One hot encoder
# I think to 'one-hot' encode your data is to assign categories of 1 or 0 to labels
# to do this use pandas' 'get_dummies'
print ''
print "One-hot encoder using pandas = pandas.get_dummies(data['health']): "
print pandas.get_dummies(data['health'])

# We could do this in sklearn on the label encoded data using OneHotEncoder as follows:
print ''
print "One-hot encoder using sklearn: "


ohe = preprocessing.OneHotEncoder() # creating OneHotEncoder object
label_encoded_data = label_encoder.fit_transform(data['health'])
ohe.fit_transform(label_encoded_data.reshape(-1, 1))
print 'ohe.fit_transform(label_encoded_data.reshape(-1, 1)):'
print ohe.fit_transform(label_encoded_data.reshape(-1, 1))

