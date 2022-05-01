# Exercicio 1
import datetime as dt

def datetime_to_excel(date: dt.datetime) -> int:

    start_date = dt.datetime(1899, 12, 31)

    diff_to_start = date - start_date
    
    return int(diff_to_start.days)

def excel_to_datetime(date: int) -> dt.datetime:

    start_date = dt.datetime(1899, 12, 31)

    days_to_add = dt.timedelta(days = date)

    datetime_date = start_date + days_to_add

    return datetime_date


teste_excel = datetime_to_excel(dt.datetime(2018, 1, 2))
print(teste_excel)

teste_datetime = excel_to_datetime(43101)
print(teste_datetime)
