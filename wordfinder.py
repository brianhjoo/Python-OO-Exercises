class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        """ takes a path to a text file, extracts list of words, prints
            message: [num-of-words-read] words read """

        self.path = path
        self.list_of_words = []
        # self.print_message

    def extract_words(self) :
        """ read file and extract words to list_of_words """

        file = open(self.path)

        for line in file:
            self.list_of_words.append(line[:-1])