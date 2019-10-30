# Libraries

import os
import re
from dataclasses import dataclass
from datetime import date

# Opening the motivation letter (in .pages format)
@dataclass
class LmParser:

    input_file: str
    output_file: str
    old_words: tuple
    new_words: tuple

    def __post_init__(self):

        self.lm_words_replace()
        self.display_new_cover_letter()

    def lm_words_replace(self):

        """
        This function intends to help people that are applying to lot of jobs by allowing him to automatically replace the keywords
        in his cover letter according to the job requirements (such as the name of the company, the role of the job, the datetime, etc...).
        This function will thus, allow the user to gain a lot of time and to avoid typing mistakes while modifying its cover letter.
        ------
        Parameters:
            - old_words : a set containing all the words to replace in the cover letter.
            - new_words : a set containing all the words to put in the cover letter instead of the old ones.
            - input_file : the name of the cover letter file.
            - output_file : the newly generated cover letter with the keywords modified by the user.
        """

        read_file = open(self.input_file, "rt")
        write_file = open(self.output_file, "wt")

        for line in read_file:
            for old, new in zip(self.old_words, self.new_words):
                line = line.replace(old, new)
            write_file.write(line)

        read_file.close()
        write_file.close()

        my_text = open(self.input_file, "rt")
        print(my_text.read())

    # Overview of the new cover letter
    def display_new_cover_letter(self):

        my_text_2 = open(self.output_file, "rt")
        print(my_text_2.read())


if __name__ == '__main__':

    old_words = ('October 11, 2016', 'Employment Manager', 'IT services and consulting corporation')
    new_words = ('03 Octobre 2019', 'Data Scientist', 'New Company')
    input_file = 'my_cover_letter.txt'
    output_file = 'test.txt'
    LmParser(input_file, output_file, old_words, new_words)
    print('Process finished')






