my_list = [1, 2, 5, 6]

my_list2 = ['plotly', 'is', 'awesome']  # define another list

my_list3 = my_list + my_list2  # concatenate

my_list3.append(100)        # append just a single item

my_list3.append(my_list2)   # append list with list

my_list3

my_list3_ref = my_list3  # variables my_list_ref and my_list3 refer to same list

my_list3[4] = 'PLOTLY'   # changing item in my_list3 affects my_list3_ref

my_list3_ref

my_list3_ref[6] = 'AWESOME' # changing item in my_list3_ref affects my_list3

my_list3_sc = list(my_list3)  # assign a shallow copy of my_list3 to my_list3_sc,
                              #   same as my_list3_sc = my_list3[:]

my_list3[4] = 'PlOtLy'    # changes non-nested item in my_list3, not my_list3_sc

my_list3_sc[6] = 'AwEsOmE'  # changes non-nested item in my_list3_sc, not my_list3


print(my_list3)
print(my_list3[-1][0])  # first item in nested list of last item in my_list3
print (my_list3_ref)
print(my_list3_sc)

