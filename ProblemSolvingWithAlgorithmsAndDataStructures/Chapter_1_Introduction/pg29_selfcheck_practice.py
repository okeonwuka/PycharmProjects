import random


# create alphabet characters including 'space' character
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                 'y', 'z', ' ']

# create empty list to house character matches from target sentence
sentence_generator = []


# # define random_alphabet_selector function (version 1)
# def random_alphabet_selector():
#     global selected_alphabet
#     selected_alphabet = random.choice(alphabet_list)
#     return selected_alphabet


# define random_alphabet_selector function (version 2 - simpler)
def random_alphabet_selector():
    return random.choice(alphabet_list)


# Input target sentence
target_sentence = input('Please enter desired sentence:')
print('your target sentence is: %s ' % target_sentence)


# # Monkey theorem algorithm test version 1
# for i in range(100):
#     for a_character in target_sentence:
#         random_alphabet_selector()
#         if a_character == random_alphabet_selector():
#             print('There is a match')
#             sentence_generator.append(random_alphabet_selector())
#         else:
#             print('No match')
# print(sentence_generator)


# # Monkey theorem algorithm test version 2
# for i in range(500):
#     for a_character in target_sentence:
#         selected_alphabet = random_alphabet_selector()
#         if a_character == selected_alphabet:
#             print('yes there is a match, %s is in the target sentence' % selected_alphabet)
#             if selected_alphabet in sentence_generator:
#                 pass
#             else:
#                 sentence_generator.append(selected_alphabet)
#         else:
#             print('No match')
# print(sentence_generator)


# Monkey theorem algorithm test version 2
for i in range(10000):
    for a_character in target_sentence:
        selected_alphabet = random_alphabet_selector()
        if a_character == selected_alphabet:
            print('yes there is a match, %s is in the target sentence' % selected_alphabet)
            sentence_generator.append(selected_alphabet)
        else:
            print('No match')


# combine items in the sentence_generator into a string and store in a variable called penultimate_sentence_generator
penultimate_sentence_generator = ''.join(sentence_generator)
print('The penultimate sentence generator is: %s' % penultimate_sentence_generator)


# Delimit/split the string in penultimate_sentence_generator by ' ' (space) and place in final_sentence_generator
final_sentence_generator = penultimate_sentence_generator.split(' ')
print('The Final sentence generated is: %s' % final_sentence_generator)


for a_word in final_sentence_generator:
    word_count = final_sentence_generator.count(a_word)
    for i in range(word_count):
        if len(a_word) < 28:
            final_sentence_generator.remove(a_word)
print('The final 27 character words are:  %s' % final_sentence_generator)











