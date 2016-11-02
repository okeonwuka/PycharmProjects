#  importing itemgetter allows us to sort on multiple levels of sorting

from operator import itemgetter


def count_words(input_sentence, n):
    # Convert input sentence into a list of words
    list_of_words = input_sentence.split(' ')

    # Sort list alphabetically
    list_of_words.sort()

    # Create a list to hold word count from 'list_of_words'
    word_count_list = []

    # Fill up 'word_count_list'  with number of occurrence/
    # frequency of each word from the input sentence

    for item in list_of_words:
        lc_word_count_variable = list_of_words.count(item)
        word_count_list.append(lc_word_count_variable)

    # Use python function to pair a word to its respective count,
    # thus generating  a 'List of Tuples'. ie pair
    # list_of_words and word_count_list
    list_of_tuples = list(zip(list_of_words, word_count_list))

    # Remove duplicates
    unique_list_of_tuples = []
    for item in list_of_tuples:
        if item not in unique_list_of_tuples:
            unique_list_of_tuples.append(item)

    # unique_list_of_tuples.sort(key =lambda tup: tup[1], reverse=True)

    # First stage sort:  sort by second item in tuple, in reverse order (descending order)
    sorted_unique_list_of_tuples = sorted(unique_list_of_tuples, key=itemgetter(1), reverse=True)

    # Second stage sort: sort by first item in tuple, ascending order
    sorted(sorted_unique_list_of_tuples, key=itemgetter(0))

    #     >> s = sorted(student_objects, key=attrgetter('age'))     # sort on secondary key
    # >>> sorted(s, key=attrgetter('grade'), reverse=True)       # now sort on primary key, descending


    # print and return first n items in unique_list_of_tuples, which by the code
    # corresponds to the top n words with highest count. To do this just
    # slice list
    top_n = print(sorted_unique_list_of_tuples[:n])
    return top_n


# count_words('nothing is wrong with i and i but i will wrong i', 9)

# count_words('betty bought a bit of butter but the butter was bitter', 3)

count_words(
    'Knowing that millions of people around the world would be watching in person and on television and expecting great things from him at least one more gold medal for America if not another world'
    ' record during this his fourth and surely his last appearance in the World Olympics and realizing that his legs could no longer carry him down the runway with the same blazing speed and confidence in '
    'making a huge eye popping leap that they were capable of a few years ago when he set world records in the 100 meter dash and in the 400-meter relay and won a silver medal in the long jump the renowned '
    'sprinter and track and field personality Carl Lewis who had known pressure from fans and media before but never even as a professional runner, this kind of pressure made only a few appearances in races during '
    'the few months before the Summer Olympics in Atlanta Georgia partly because he was afraid of raising expectations even higher and he did not want to be distracted by interviews and adoring fans who would'
    ' follow him into stores and restaurants demanding autographs and photo opportunities but mostly because he wanted to conserve his energies and concentrate like a martial arts expert on the job at hand winning '
    'his favorite competition the long jump and bringing home another Gold Medal for the United States the most fitting conclusion to his brilliant career in track and field Knowing that millions of people around the world would be watching in person and on television and expecting great things from him at least one more gold medal for America if not another world'
    ' record during this his fourth and surely his last appearance in the World Olympics and realizing that his legs could no longer carry him down the runway with the same blazing speed and confidence in '
    'making a huge eye popping leap that they were capable of a few years ago when he set world records in the 100 meter dash and in the 400-meter relay and won a silver medal in the long jump the renowned '
    'sprinter and track and field personality Carl Lewis who had known pressure from fans and media before but never even as a professional runner, this kind of pressure made only a ,  few appearances in races during '
    'the few months before the Summer Olympics in Atlanta Georgia partly because he was afraid of raising expectations even higher and he did not want to be distracted by interviews and adoring fans who would'
    ' follow him into stores and restaurants demanding autographs and photo opportunities but mostly because he wanted to conserve his energies and concentrate like a martial arts expert on the job at hand winning '
    'his favorite competition the long jump and bringing home another Gold Medal for the United States the most fitting conclusion to his brilliant career in track and field',
    1000)
