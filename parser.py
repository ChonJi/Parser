import codecs
import re

class Parser:

    __file__ = None
    __my_list__ = []
    __document__ = None

    def __init__(self, document):
        self.__document__ = document

    def __parse_file__(self):
        with codecs.open(self.__document__, 'r', 'utf-8') as self.__file__:
            return self.__file__.read()

    def print_file(self):
        print(self.__parse_file__())

    def count_words(self, searched_phase):

        searched_word_number = 0
        all_words_number = 0
        file = re.findall('\w+', self.__parse_file__().lower())

        for word in file:
            self.__my_list__.append(word)
            if searched_phase.lower() in word:
                searched_word_number += 1
                all_words_number += 1
                print(word.capitalize() + ', place: ' + str(all_words_number))

            else:
                all_words_number += 1

        print(searched_phase.capitalize() + ', the number of occurrences: ' + str(searched_word_number))
        print('Number of words in document: ' + str(all_words_number))

    def print_list(self):
        print(self.__my_list__)



p = Parser('test.txt')
p.print_file()
print()
p.count_words('dolore')
print()
p.print_list()





