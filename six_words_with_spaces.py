from random import sample, randint
import word_with_blanks

class Six_words_with_blanks:

    def __init__(self):
        self.words = ""

    def generate_six_words_with_blanks(self, word):
        word_len = len(word)
        num_spaces = 1
        # letters_remain = word_len - num_spaces
        for i in range(0, 6):
            word_containing_blanks = word_with_blanks.Word_with_blanks(word)
            if word_len - num_spaces >= 0:
                self.words += word_containing_blanks.insert_blanks_in_word(num_spaces) + ", "
            else:
                self.words += word_containing_blanks.insert_blanks_in_word(randint(1, word_len)) + ", "
            num_spaces += 1
        return self.words[:-2]
