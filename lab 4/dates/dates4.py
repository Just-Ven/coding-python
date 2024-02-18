import datetime

def diffInSeconds(date1, date2):
    difference = date2 - date1
    differenceInSec = difference.total_seconds()
    return differenceInSec


date1 = datetime.datetime(2019, 1, 1, 12, 0, 0)  # year - month - day - hour - minute - second
date2 = datetime.datetime(2024, 1, 1, 12, 0, 10)

difference_seconds = diffInSeconds(date1, date2)
print(difference_seconds)
