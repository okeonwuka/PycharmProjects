#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

from __future__ import division # The line below enables division of a/b not to be zero where a<b in python2
import pickle
import numpy as np
import pandas as pd



enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# ========================================================================================================================================================

# Quiz Questions:
# 1. How many data points/people are in the enron data set
print '1. How many data points/people are in the enron data set?'
numberOfPeopleInEnronDataSet = len(enron_data)
print 'The number of people in the enron_data set is: {}'  .format(numberOfPeopleInEnronDataSet)
print ''
# ========================================================================================================================================================

# print enron_data
# listOfValues = []
# listOfValues2 = []
# for v in enron_data.values():
#     listOfValues.append(v)
# print listOfValues
# print len(listOfValues)
# ========================================================================================================================================================

# 2. For each person, how many features are available?
print '2. How many features are available? '
print 'The number of features are the same for each person/Key. So i found the length of on person/key in the data ie METTS MARK '
print 'and I found the length of the dictionary of features associated with this person/key'
print 'The dictionary to be observed belongs to a person called METTS MARK and is: {}'.format(enron_data['METTS MARK'])
print ' The number of features available is: {}'.format(len(enron_data['METTS MARK']))



# for topkey in enron_data:
#     for key in enron_data['METTS MARK']:
#         listOfValues2.append(key)

# print len(listOfValues2)
# enron_data

print ''
# ========================================================================================================================================================

# 3. How many person of interest (POI) in the data set?
print '3. How many person of interest (POI) in the data set? '

# This function finds all occurences of a key in nested python dictionaries and lists. 
# Credit https://gist.github.com/douglasmiranda/5127251
# Create find function
# Function definition:
def find(key, dictionary):
    for k, v in dictionary.iteritems():
        if k == key:
            yield v
        elif isinstance(v, dict):
            for result in find(key, v):
                yield result
        elif isinstance(v, list):
            for d in v:
                for result in find(key, d):
                    yield result



listOfValuesWhoseKeyIs_poi = list(find('poi', enron_data))

numberOfPOI_InEnronData = listOfValuesWhoseKeyIs_poi.count(True)
print 'The number of people of Interest (POI) in the enron_data set is: {}'  .format(numberOfPOI_InEnronData)
print ''
# ========================================================================================================================================================

print '4. What is the total value of the stock belonging to James Prentice?'
print enron_data['PRENTICE JAMES']['total_stock_value']
print ''
# print enron_data.keys()
# ========================================================================================================================================================


print '5. How many email messages do we have from Wesley Colwell to persons of interest?'
print enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print ''
# ========================================================================================================================================================

print '6. Whats the value of stock options exercised by Jeffrey K Skilling?'
print enron_data['SKILLING JEFFREY K']['exercised_stock_options']
print ''
# ========================================================================================================================================================

print '7. Who took the most money?'
# print enron_data.keys()
print 'FASTOW ANDREW S took ${}'.format(enron_data['FASTOW ANDREW S']['total_payments'])
print 'LAY KENNETH L took ${}'.format(enron_data['LAY KENNETH L']['total_payments'])
print 'SKILLING JEFFREY K took ${}'.format(enron_data['SKILLING JEFFREY K']['total_payments'])
print ''
# ========================================================================================================================================================

print '8. How many folks in the data set have a quantified salary, known email address?'

# Calculate quantified salary
listOfSalary = list(find('salary',enron_data))
countOfSalary = len(listOfSalary)
countOfUnknownSalary = listOfSalary.count('NaN')
countOfknownSalary = countOfSalary - countOfUnknownSalary

# Calculate known email address
listOfEmailAddy = list(find('email_address', enron_data))
countOfEmailAddy = len(listOfEmailAddy)
countOfUnknownEmailAddy = listOfEmailAddy.count('NaN')
countOfKnownEmailAddy = countOfEmailAddy - countOfUnknownEmailAddy

print 'The number of people with known salary and email addresses are {} and {} respt'  .format(countOfknownSalary,countOfKnownEmailAddy)
print ''
# ========================================================================================================================================================

# Create a division function
# Function definition:
def divide(A,B):
    return A/B

print '9. How many people in the E+F dataset (as it currently exists) have NaN for their total payments?'
print '   What percentage of people in the dataset as a whole is this?'

listOfTotalPayments = list(find('total_payments', enron_data))
countOf_NaN_totalPayments = listOfTotalPayments.count('NaN')
print '   {} people in the E+F dataset have NaN for their total payments'.format(countOf_NaN_totalPayments)

percentageOfPeopleWith_NaN_forTotalPayments = divide(countOf_NaN_totalPayments,numberOfPeopleInEnronDataSet) *100
print '   This is {}%  of people in the dataset' .format(percentageOfPeopleWith_NaN_forTotalPayments)
print ''
# ========================================================================================================================================================

print '10. What percentage of POIs in the dataset have NaN for their total payments?'

"""
    # for item in enron_data:
    #         for k,v in item:
    #             if k == 'total_payments' & v == 'NaN':
    #                 print k

    poi_list = []
    total_payments_list = []
        
    for key, dictionary in enron_data.items():
        for innerkey in dictionary:
            if innerkey == 'poi':
                #print dictionary[innerkey]
                poi_list.append(dictionary[innerkey])
                print poi_list
            if innerkey == 'total_payments':
                #print dictionary[innerkey]
                total_payments_list.append(dictionary[innerkey])
                print total_payments_list

               
     # Use python function to pair a innerkey 'poi' 
     # to its innerkey ' total_payments'
     # thus generating  a 'List of Tuples'. 
     # ie pair
     # poi_list and total_payments_list
    list_of_tuples = list(zip(poi_list, total_payments_list))
    print list_of_tuples


    # j = map( lambda (poi,_): True, filter( lambda (_,total_payments): total_payments == 'NaN', list_of_tuples) )
    # print j.count(True)


    print '=========================================================================================================================================='


    # enron_data_pandas_rep = pd.DataFrame(enron_data, columns=['bonus', 'deferral_payments','deferred_income','director_fees', 'email_address',
    #     'exercised_stock_options', 'expenses','from_messages', 'from_poi_to_this_person','from_this_person_to_poi', 'loan_advances','long_term_incentive', 'other','poi', 'restricted_stock',
    #     'restricted_stock_deferred', 'salary','shared_receipt_with_poi', 'to_messages','total_payments', 'total_stock_value'])

    enron_data_pandas_rep = pd.DataFrame(enron_data)
    print enron_data_pandas_rep

    # print enron_data_pandas_rep.loc['poi'] == True

    # Selection of multiple random columns(which are people names in this case ) from a dataframe. Format below
    print enron_data_pandas_rep[['YEAGER F SCOTT', 'WODRASKA JOHN', 'SKILLING JEFFREY K']]
    print ''
    print ''

    # Selection of a single column format
    print enron_data_pandas_rep['WODRASKA JOHN']
    print ''
    print ''

    # Selection of values of a single column:
    print enron_data_pandas_rep['WODRASKA JOHN'].values

    print enron_data_pandas_rep.loc['poi']

    print ''
    print ''

    # enron_data_pandas_rep.loc[lambda df: df.poi == True]




    # p = enron_data_pandas_rep[enron_data_pandas_rep['poi']==True]

    t = enron_data_pandas_rep.applymap(lambda poi: 'poi' == True)

    # print t[t['poi'] == True]

    print t.loc['poi'] == True

    enron_data_pandas_rep[[]]


    print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
    print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'

"""

#Solution
# 1.Calculate how many POI have total_payments as 'NaN': 

count = 0
for k in enron_data:
    if enron_data[k]['poi'] == True and enron_data[k]['total_payments'] == "NaN":
        count += 1

print '    The number of POI with total_payments = NaN is {}.' .format(count)

# 2. Calculate the number of POI.
print '    From question 3, the number of POI is {}' .format(numberOfPOI_InEnronData)

print '    Therefore the percentage POI in dataset that have NaN for their total payments is {}%' .format(divide(count,numberOfPOI_InEnronData) *100)
print ''
# ========================================================================================================================================================

print '11. If 10 more data points(which are all POI with NaN for their total_payments) are added to the dataset'
print '    what is the new number of people in the dataset and the new number of folks with NaN for total payments?'

# Solution:
print '    If 10 more data points added, with features as stated above the number of people in the dataset will be {}' .format(numberOfPeopleInEnronDataSet + 10)

# calculate the (total) number of people with total_payments == NaN (not just POI's)....if 10 new data points added with given conditions.
oldCount0fPeopleWithNaN_as_total_payment = 0
for k in enron_data:
    if enron_data[k]['total_payments'] == 'NaN':
        oldCount0fPeopleWithNaN_as_total_payment += 1
newCount0fPeopleWithNaN_as_total_payment = oldCount0fPeopleWithNaN_as_total_payment + 10

print '    If 10 more data points added, with features as stated above, the new number of folks with NaN for total payments is {}' .format(newCount0fPeopleWithNaN_as_total_payment)
print ''
# ========================================================================================================================================================

print "12. What is the new number of POIs in the dataset? What is the new number of POIs with NaN for total_payments?"

# Solution:
print '    If 10 new POIs are added, the new number of POIs is {}' .format(numberOfPOI_InEnronData + 10)
print '    and the new number of POIs with NaN for total_payments is {}' .format(count + 10)

print 'an unsupervised classification algorithm can interpret "NaN" for total_payments as a clue that some one is a POI because, all new 10 datapoints are POI and have NaN for total_payments'