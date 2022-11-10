from datetime import datetime
from datetime import timedelta


now = datetime.now()
print(now, ' - This is now')


def passed_time():
    plus_time = now + timedelta(days=1)
    print(plus_time, 'This is plus one day from now')


# passed_time()