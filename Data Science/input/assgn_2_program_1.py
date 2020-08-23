import random
import string
import pandas as pd
from datetime import datetime

# Question 1

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

files = {}


for i in range(500):
    
    text = ''

    for j in range(20000):
        random_word = get_random_string(20)
        text += random_word + '\n'

    files[str(i) + '_file'] = text
