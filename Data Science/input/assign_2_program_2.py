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



# Question 2
start = datetime.now()

time_taken = {}

for count, (key, value) in enumerate(files.items()):

    files[key] = value.upper()

    if (count+1)%100 == 0:
        end = datetime.now()
        time_taken[count+1] = end-start

time = [int(str(i).split('.')[-1])//1000 for i in time_taken.values()]

df = pd.DataFrame()
df['No. of files'] = time_taken.keys()
df['Time (sec)'] = time
df.to_csv('assignment_2.csv', index=False)