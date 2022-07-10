import pandas as pd
import random as rand
import numpy as np
import matplotlib as mat
from matplotlib import pyplot
from datetime import datetime as dt
from datetime import date
from datetime import timedelta


# set up variable to get the year

today = date.today()
database = pd.read_csv('sampledata.csv')



print(database)


new_income: int
new_expense: int
new_savings: int
new_total: int

# get user input for new row in db


new_income = int(input("Enter new income: $"))
new_expense = int(input("Enter new expense: $"))
new_savings = int(input("Enter savings: $"))
new_total = new_income - new_expense - new_savings



new_db_entry = pd.DataFrame({
    "DATE (YYYY-MM-DD)": [today],
    'INCOME': [new_income],
    'EXPENSES': [new_expense],
    'SAVINGS': [new_savings],
    'TOTAL': [new_total]
}, index=False)

new_db_entry.to_csv('sampledata.csv', mode='a', index=False, header=False)

print("\n\nHere is the new data in the database:\n\n")
print(pd.read_csv('sampledata.csv'))

