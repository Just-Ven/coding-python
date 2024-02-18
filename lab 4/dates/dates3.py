import datetime

def delMicroSec(x):
    return x.replace(microsecond = 0)

current_datetime = datetime.datetime.now()
new_time = delMicroSec(current_datetime)

print(new_time)