from datetime import datetime
from datetime import time as dt_time
from datetime import timedelta

import arrow

import constants as cs


def calc_date():
    my_now = arrow.now('Europe/Moscow')
    return my_now


def times_of_remind():
    local_now = arrow.now()
    my_now_with_zero_time = datetime.combine(local_now.date(), dt_time())

    my_now_with_zero_date = datetime.combine(datetime.min.date(), calc_date().time())
    local_now_with_zero_date = datetime.combine(datetime.min.date(), local_now.time())
    dif_timedelta = my_now_with_zero_date - local_now_with_zero_date

    first_remind_at = (
            my_now_with_zero_time + timedelta(hours=cs.first_time_h, minutes=cs.first_time_m) - dif_timedelta).strftime(
        '%H:%M:%S')
    second_remind_at = (
            my_now_with_zero_time + timedelta(hours=cs.second_time_h,
                                              minutes=cs.second_time_m) - dif_timedelta).strftime(
        '%H:%M:%S')

    return first_remind_at, second_remind_at


def month_name():
    month_name = calc_date().strftime('%B')
    return month_name


def hello():
    weekdayname = calc_date().strftime('%A').upper()
    hello_text = 'Привет, напоминаю тебе, что сегодня {}' \
                 ' и у тебя тренировка по расписанию. ' \
                 'Будешь заниматься сейчас или позже?'.format(weekdayname)
    return hello_text
