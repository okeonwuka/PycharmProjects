input_sentence = 'I am a boy boy and I like to go I do'


def function count_words(input_sentence, number)

:

# create variables to be used:

# Break up input sentence string into a list of words
list_of_words = input_sentence.split(' ')

print(list_of_words)
print('=============================================================')
print('=============================================================')
finalList = []
OccurenceList = []
OccurenceListholder = []

for word in split_Sentence_String:
    OccurenceListholder = split_Sentence_String.count(word)
    OccurenceList.append(OccurenceListholder)

print(OccurenceList)
print('=============================================================')
print('=============================================================')

print('=============================================================')

print(list(zip(split_Sentence_String, OccurenceList)))
