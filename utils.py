from datetime import datetime
from datetime import time as dt_time
from datetime import timedelta

import arrow


def calc_dates():
    local_now = arrow.now()
    my_now = arrow.now('Europe/Moscow')
    weekdayname = my_now.strftime('%A').upper()
    month_name = my_now.strftime('%B')

    my_now_with_zero_time = datetime.combine(local_now.date(), dt_time())

    my_now_with_zero_date = datetime.combine(datetime.min.date(), my_now.time())
    local_now_with_zero_date = datetime.combine(datetime.min.date(), local_now.time())
    dif_timedelta = my_now_with_zero_date - local_now_with_zero_date

    first_time_h, first_time_m = 10, 0  # work at 10:00
    second_time_h, second_time_m = 23, 0  # work at 23:00
    first_remind_at = (
        my_now_with_zero_time + timedelta(hours=first_time_h, minutes=first_time_m) - dif_timedelta).strftime(
        '%H:%M:%S')
    second_remind_at = (
        my_now_with_zero_time + timedelta(hours=second_time_h, minutes=second_time_m) - dif_timedelta).strftime(
        '%H:%M:%S')

    hello_text = 'Привет, напоминаю тебе, что сегодня {}' \
                 ' и у тебя тренировка по расписанию. ' \
                 'Будешь заниматься сейчас или позже?'.format(weekdayname)

    return first_remind_at, second_remind_at, month_name, my_now