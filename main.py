import pandas as pd
import random as rand
import numpy as npy
import matplotlib as mat
from matplotlib import pyplot
from datetime import datetime as dt
from datetime import date
from datetime import timedelta
import tkinter as tkk


# set up variable to get the year

today = date.today()




# test = date(2022,7,2)  this will get now's date

sampletable = {
    'DATE (YYYY-MM-DD)': [today, today, today, today, today]
    , 'INCOME': [
        3000, 3000, 3000, 3000, 3000
    ]
    , 'EXPENSES': [
        rand.randint(100, 500),
        rand.randint(100, 500),
        rand.randint(100, 500),
        rand.randint(100, 500),
        rand.randint(100, 500)
    ]
    , 'SAVINGS': [
        rand.randint(1, 100),
        rand.randint(1, 50),
        rand.randint(1, 20),
        rand.randint(1, 100),
        rand.randint(1, 100)
    ]
}
df = pd.DataFrame(data=sampletable)
df['TOTAL'] = df['INCOME'] - df['EXPENSES'] - df['SAVINGS']




# df.to_csv('sampledata.csv', index=False)



print(df)
