import datetime

def one_day_limit(add_time):
    """
    calculates whether the given time confirms one day's limit
    add_time: given datetime
    """
    now = datetime.datetime.now()
    midnight = now.replace(day=now.day+1, hour=0, minute=0, second=0, microsecond=0)
    return (midnight - add_time) < datetime.timedelta(days=1)

def weekend():
    """
    indicates whether it is Saturday or Sunday
    """
    now = datetime.datetime.now()
    return (now.weekday() == 5) or (now.weekday() == 6)
