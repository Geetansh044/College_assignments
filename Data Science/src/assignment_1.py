import datetime
import pandas as pd
import numpy as np

l = []
number = ['5k', '10k', '15k', '20k', '25k']
time = []

for i in range(5):

    to_sort = np.random.randint(0, 5000, i*5000 + 5000)

    starttime = datetime.datetime.now()
    to_sort.sort()
    endtime = datetime.datetime.now()


    print("Time taken to sort " + str(i*5000 + 5000) + ' elements is: ', endtime-starttime)
    time.append(endtime-starttime)

    time = [str(i).split('.')[-1] for i in time]
    time = [int(i) for i in time]

df = pd.DataFrame()
df['Number of elements in list'] = number
df['Time taken to sort (ms)'] = time
df.to_csv('assignment_1.csv', index=False)