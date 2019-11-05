from .config import STOP_WORDS, _STOP_WORDS


class Parser:
    """
    Here is the class which will parse the user input in order to keep only key worlds
    """

    def __init__(self, u_input):
        
        # Making only one list of stop words, and deleting duplicates
        self.stop = []
        self.stop.extend(STOP_WORDS)
        self.stop.extend(_STOP_WORDS)
        list(set(self.stop))

        # Lowering user input
        self.user_input = u_input.lower()
        self.parsed_input_list = []
        self.parsed_input = ""

        # too short users' input are not parsed
        if len(self.user_input) >= 5:
            self.parse()


    def parse(self):

        # We split the question into words list
        split_input = self.user_input.split()

        for word in split_input:

            # way to delete punctuation
            cleaned_word = word.translate(str.maketrans('', '', '.,?!:'))
            squote = cleaned_word.find("'")

            if squote != -1:
                squote += 1

                if cleaned_word[squote:] not in self.stop:
                    self.parsed_input_list.append(cleaned_word[squote:])

            else:
                if cleaned_word not in self.stop:
                    self.parsed_input_list.append(cleaned_word)

        # we convert key world list into str
        self.parsed_input = ' '.join(self.parsed_input_list)
