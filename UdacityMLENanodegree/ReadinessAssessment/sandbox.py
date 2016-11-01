input_sentence = 'i am a boy boy and i like to go i do'
list_of_words = input_sentence.split(' ')
print('List of Words =  ', list_of_words)

print(
    '==========================================================================================================================')
print(
    '==========================================================================================================================')
word_freq_count_list = []

for item in list_of_words:
    lc_word_freq_count_list = list_of_words.count(item)
    word_freq_count_list.append(lc_word_freq_count_list)
print('Frequency count of words in List = ', word_freq_count_list)

print(
    '==========================================================================================================================')
print(
    '==========================================================================================================================')

list_of_tuples = list(zip(list_of_words, word_freq_count_list))
print('The list of Tuples = ', list_of_tuples)

# Remove duplicates

unique_list_of_tuples = []

for item in list_of_tuples:
    if item not in unique_list_of_tuples:
        unique_list_of_tuples.append(item)

print(
    '==========================================================================================================================')
print(
    '==========================================================================================================================')

print('The Unique  list of Tuples = ', unique_list_of_tuples)

# sort unique list of Tuples
# unique_list_of_tuples.sort()

print(
    '==========================================================================================================================')
print(
    '==========================================================================================================================')

print('The sorted Unique  list of Tuples = ', unique_list_of_tuples)

# sort by second item in tuple
unique_list_of_tuples.sort(key=lambda tup: tup[1], reverse=True)
# sort by second item in tuple
# unique_list_of_tuples.sort(key =lambda tup: tup[1] )


print('The sorted Unique  list of Tuples by second item = ', unique_list_of_tuples)
