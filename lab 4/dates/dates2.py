# Write a Python program to print yesterday, today, tomorrow.
import datetime

def printYesterday():
    current_date = datetime.datetime.now()
    yesterday = current_date - datetime.timedelta(1)
    return yesterday

print(printYesterday())


def printToday():
    current_date = datetime.datetime.now()
    return current_date

print(printToday())


def printTomorrow():
    current_date = datetime.datetime.now()
    tomorrow = current_date + datetime.timedelta(1)
    return tomorrow

print(printTomorrow())

