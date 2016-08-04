# Removing duplicates for a list

# create lists
word_list = ['cat', 'dog', 'rabbit']
letter_list = []

# iteration with 'for', selection with 'if'
# Depending on where you put the print statement you get diff various output



# 1. print function/statement closes first for loop - Desired result
for a_word in word_list:
     for a_letter in a_word:
         letter_list.append(a_letter)
         for item in letter_list:
             if letter_list.count(item)> 1:
                 letter_list.remove(item)
print(letter_list)


# # 2. print function/statement closes 2nd for loop
# for a_word in word_list:
#      for a_letter in a_word:
#          letter_list.append(a_letter)
#          for item in letter_list:
#              if letter_list.count(item)> 1:
#                  letter_list.remove(item)
#      print(letter_list)
#


# # 3. print function/statement closes 3rd for loop
# for a_word in word_list:
#      for a_letter in a_word:
#          letter_list.append(a_letter)
#          for item in letter_list:
#              if letter_list.count(item)> 1:
#                  letter_list.remove(item)
#          print(letter_list)


# # 3. print function/statement closes if statement
# for a_word in word_list:
#      for a_letter in a_word:
#          letter_list.append(a_letter)
#          for item in letter_list:
#              if letter_list.count(item)> 1:
#                  letter_list.remove(item)
#              print(letter_list)





