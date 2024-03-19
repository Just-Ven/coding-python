import datetime

def dropMicroSec(x):
    return x.replace(microsecond = 0)

current_datetime = datetime.datetime.now()
new_time = dropMicroSec(current_datetime)

print(new_time)