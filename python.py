# Exercício 1
# importing libraries
import datetime as dt

def datetime_to_excel(date: dt.datetime) -> int:
    
    '''Converts a datetime object to an int
    that representes a serial excel date'''

    start_date = dt.datetime(1899, 12, 31)

    diff_to_start = date - start_date

    return int(diff_to_start.days)


def excel_to_datetime(date: int) -> dt.datetime:
    
    '''Converts a serial excel date to a
    datetime object'''
    
    start_date = dt.datetime(1899, 12, 31)

    days_to_add = dt.timedelta(days = date)

    datetime_date = start_date + days_to_add

    return datetime_date

# validating results
test_excel = datetime_to_excel(dt.datetime(2018, 1, 2))
print(test_excel)

test_datetime = excel_to_datetime(43101)
print(test_datetime)

# Exercicio 2

# importing libraries
import os
import pandas as pd

# getting working directory
wd = os.getcwd()

# reading dataframe and renaming columns
shares_df = pd.read_csv(wd + "/tabela_acoes.csv").rename(columns = {
    "Ação":"ticker",
    "Cliente":"client",
    "QTD":"qtd",
    "PREÇO":"price"
})

# calculating total invested amount per client
shares_df.loc[:, "invested_amount"] = shares_df.loc[:, "qtd"] * shares_df.loc[:, "price"]
total_invested_per_client = shares_df.groupby("client").invested_amount.sum().reset_index()

total_invested_per_client