import codecs
import re

class Parser:

    file = None
    my_list = []

    def parse_file(self, document):
        with codecs.open(document, 'r', 'utf-8') as self.file:
            return self.file.read()

    def print_file(self, document):
        print(self.parse_file(document))

    def count_words(self, document, searched_phase):

        searched_word_number = 0
        all_words_number = 0
        file = re.findall('\w+', self.parse_file(document).lower())

        for word in file:
            self.my_list.append(word)
            if searched_phase.lower() in word:
                searched_word_number += 1
                all_words_number += 1
                print(word.capitalize() + ', place: ' + str(all_words_number))

            else:
                all_words_number += 1

        print(searched_phase.capitalize() + ', the number of occurrences: ' + str(searched_word_number))
        print('Number of words in document: ' + str(all_words_number))

    def print_list(self):
        print(self.my_list)



p = Parser()
p.print_file('test.txt')
print()
p.count_words('test.txt', 'dolore')
p.print_list()




