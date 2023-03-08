from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        """ takes a path to a text file, extracts list of words, prints
            message: [num-of-words-read] words read """

        self.path = path
        self.list_of_words = self.extract_words()
        self.printNumOfWordsRead()

    def extract_words(self) :
        """ read file and extract words to list_of_words """

        list_of_words = []

        file = open(self.path)

        for line in file:
            list_of_words.append(line[:-1])

        file.close()

        return list_of_words

    def printNumOfWordsRead(self):
        """ gets the number of extracted words from the file in path and
        prints that number out when making a new class """

        print(f'{len(self.list_of_words)} words read')

    def random(self):
        """ returns a random word from list_of_words """

        return choice(self.list_of_words)

class SpecialWordFinder(WordFinder):
    """ SpecialWordFinder: filters out #comments and empty lines from a
    dictionary """

    def __init__(self, path):
        """ inherits class WordFinder's attributes and methods """
        super().__init__(path)

    def extract_words(self):
        """ gets a list of all file items in the original file, then returns
        a list of those items without #comments or empty lines included """

        list_of_words = []

        all_extracted_text = super().extract_words()

        for value in all_extracted_text:
            if value.strip() and not value.strip()[0] == '#':
                list_of_words.append(value)

        return list_of_words







