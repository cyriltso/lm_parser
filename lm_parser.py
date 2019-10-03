### Libraries

import os
import re
from datetime import date

### Opening the motivation letter (in .pages format)

my_text = open("your_cover_letter", "rt")
print(my_text.read())

### Creating a function that allows to replace elements in a cover letter

old_words = ('Datetime', 'Role', 'Company')
new_words = ('03 Octobre 2019', 'Data Scientist', 'New Company')

def lm_words_replace(old_words, new_words, input_file, output_file):
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
    
    read_file = open(input_file, "rt")
    write_file = open(output_file, "wt")
    
    for line in read_file:
        for old, new in zip(old_words, new_words):
            line = line.replace(old, new)
        write_file.write(line)
        
    read_file.close()
    write_file.close()

### Replacing contents in a .txt file with new contents

input_file = "your_cover_letter"
output_file = 'test.txt'

lm_words_replace(old_words, new_words, input_file, output_file)

### Overview of the new cover letter

my_text_2 = open("test.txt", "rt")
print(my_text_2.read())