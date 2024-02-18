import datetime

def subtract_five_days():
    current_date = datetime.datetime.now()
    five_days_ago = current_date - datetime.timedelta(days=5)
    return five_days_ago

print(subtract_five_days())
