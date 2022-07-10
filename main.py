import pandas as pd
import random as rand
import numpy as np
import matplotlib as mat
from matplotlib import pyplot as plt
from datetime import datetime as dt
from datetime import date
from datetime import timedelta


# set up variable to get the year

today = date.today()
new_income: int
new_expense: int
new_savings: int
new_total: int
choice: str
database: pd.DataFrame
is_correct: str

menu = "Enter new row:\tnew\nGet total balance:\tbalance\nGet total expenses:\texpenses\nQuit:\tquit"
menu += "\nPlot graph:\tgraph"

# get user input for new row in db

choice = input(f"What do you want to do?\n{menu}\n\n")

while True:

    if choice.lower() == "quit":
        print(pd.read_csv('sampledata.csv').tail())
        break

    elif choice.lower() == 'new':
        new_income = int(input("Enter new income: $"))
        new_expense = int(input("Enter new expense: $"))
        new_savings = int(input("Enter savings: $"))
        new_total = new_income - new_expense - new_savings
        new_db_entry = pd.DataFrame({
            "DATE": [today],
            'INCOME': [new_income],
            'EXPENSES': [new_expense],
            'SAVINGS': [new_savings],
            'TOTAL': [new_total]
        })
        is_correct = input(f"Is this correct?\n{new_db_entry}\n(y/n)\t")
        # get next attempt data and ask again if the data entered is correct
        if is_correct.lower() == "n":
            while True:
                new_income = int(input("Enter new income: $"))
                new_expense = int(input("Enter new expense: $"))
                new_savings = int(input("Enter savings: $"))
                new_total = new_income - new_expense - new_savings
                new_db_entry = pd.DataFrame({
                    "DATE": [today],
                    'INCOME': [new_income],
                    'EXPENSES': [new_expense],
                    'SAVINGS': [new_savings],
                    'TOTAL': [new_total]
                })
                is_correct = input(f"Is this correct?\n{new_db_entry}\n(y/n)\t")
                if is_correct.lower() == 'y':
                    break
        # add new row to the csv file.
        new_db_entry.to_csv('sampledata.csv', mode='a', index=False, header=False)

    elif choice.lower() == "balance":
        database = pd.read_csv('sampledata.csv')
        balance = database['TOTAL'].sum()
        print(f"Total balance:\t{balance}")

    elif choice.lower() == "expenses":
        database = pd.read_csv('sampledata.csv')
        expenses = database['EXPENSES'].sum()
        print(f"Total of expenses:\t{expenses}")

    elif choice.lower() == "graph":
        database = pd.read_csv('sampledata.csv')
        chart_type = input("Line Graph: line\nBar Graph: bar\n")
        x = database['DATE']
        y = database['INCOME'].sum()
        z = database['EXPENSES'].sum()
        a = database['SAVINGS'].sum()
        if chart_type.lower() == 'bar':
            plt.bar(x=["INCOME", 'EXPENSES', 'SAVINGS'], data=[y, z, a], height=y+500)
            plt.ylabel("$")
            plt.xlabel('Sum Totals')
        elif chart_type.lower() == 'line':
            plt.plot(x, y)
            plt.plot(x, z)
            plt.plot(x, a)


        plt.legend(['INCOME', 'EXPENSES', 'SAVINGS'])
        plt.show()

    choice = input(f"\n\nWhat do you want to do next?\n{menu}\n\n")


print("\n\nHere is the new data in the database:\n\n")

print(pd.read_csv('sampledata.csv'))

