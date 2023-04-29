import datetime

import pytz


def get_current_utc_datetime():
    now_utc = datetime.datetime.now(tz=pytz.UTC)
    return now_utc
