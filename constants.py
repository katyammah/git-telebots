import arrow
from datetime import datetime, timedelta, time as dt_time

wrkout1 = ['https://www.youtube.com/watch?v=8Hy4OstJzvc&list=PL1tB2Cr-gJvmH5SJD-Fl2OVm6ZIJpjUbw&index=1',
           'https://www.youtube.com/watch?v=lCJ42q1HGQw&list=PL1tB2Cr-gJvmH5SJD-Fl2OVm6ZIJpjUbw&index=8',
           'https://www.youtube.com/watch?v=lid4GfHO7U0&list=PL1tB2Cr-gJvmH5SJD-Fl2OVm6ZIJpjUbw&index=9',
           'https://www.youtube.com/watch?v=l6i3X0AWBLI&list=PL1tB2Cr-gJvmH5SJD-Fl2OVm6ZIJpjUbw&index=5']

wrkout2 = ['https://www.youtube.com/watch?v=btnAP-_GXtU&list=PL1tB2Cr-gJvmT_QJCtni0D53ayCRR-IYK&index=13',
           'https://www.youtube.com/watch?v=AgrXJRX39qA&list=PL1tB2Cr-gJvmT_QJCtni0D53ayCRR-IYK&index=11']

wrkout3 = ['https://www.youtube.com/watch?v=EPY5pfEhITo&list=LL&index=14',
           'https://www.youtube.com/watch?v=PTg7AizQViA']

local_now = arrow.now()
my_now = arrow.now('Europe/Moscow')
weekdayname = my_now.strftime('%A').upper()
month_name = my_now.strftime('%B')


my_now_with_zero_time = datetime.combine(local_now.date(), dt_time())

my_now_with_zero_date = datetime.combine(datetime.min.date(), my_now.time())
local_now_with_zero_date = datetime.combine(datetime.min.date(), local_now.time())
dif_timedelta = my_now_with_zero_date - local_now_with_zero_date

first_remind_at = (my_now_with_zero_time + timedelta(hours=22, minutes=4) - dif_timedelta).strftime('%H:%M:%S')
second_remind_at = (my_now_with_zero_time + timedelta(hours=21, minutes=59) - dif_timedelta).strftime('%H:%M:%S')

hello_text = 'Привет, напоминаю тебе, что сегодня {}' \
             ' и у тебя тренировка по расписанию. ' \
             'Будешь заниматься сейчас или позже?'.format(weekdayname)

question_text = "День подходит к концу. Уделила ли ты сегодня время спорту?"

reg_text1 = 'Ты молодец! Отдыхай!'
reg_text2 = 'Я понял. Тренировки сегодня не было'
