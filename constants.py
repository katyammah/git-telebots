import os

chat_id = os.getenv('CHAT_ID')  # (or change it for your chat_id)

wrkout1 = [
    'https://www.youtube.com/watch?v=8Hy4OstJzvc&list=PL1tB2Cr-gJvmH5SJD-Fl2OVm6ZIJpjUbw&index=1',
    'https://www.youtube.com/watch?v=lCJ42q1HGQw&list=PL1tB2Cr-gJvmH5SJD-Fl2OVm6ZIJpjUbw&index=8',
    'https://www.youtube.com/watch?v=lid4GfHO7U0&list=PL1tB2Cr-gJvmH5SJD-Fl2OVm6ZIJpjUbw&index=9',
    'https://www.youtube.com/watch?v=l6i3X0AWBLI&list=PL1tB2Cr-gJvmH5SJD-Fl2OVm6ZIJpjUbw&index=5',
]

wrkout2 = [
    'https://www.youtube.com/watch?v=btnAP-_GXtU&list=PL1tB2Cr-gJvmT_QJCtni0D53ayCRR-IYK&index=13',
    'https://www.youtube.com/watch?v=AgrXJRX39qA&list=PL1tB2Cr-gJvmT_QJCtni0D53ayCRR-IYK&index=11',
]

wrkout3 = [
    'https://www.youtube.com/watch?v=EPY5pfEhITo&list=LL&index=14',
    'https://www.youtube.com/watch?v=PTg7AizQViA',
]

btn1_text = 'Тренировка на ягодицы 🌰'
btn2_text = 'Тренировка на пресс 👟'
btn3_text = 'Тренировка на руки 💪🏼'
text_to_tomorrow = 'ОК, перенесём тренировку на завтра!'
text_tomorrow_start = 'Прошли сутки! Приступим к тренировке?'
text_ready_gym_now = 'Я подобрал тебе 3 видео с YouTube, хорошей тренировки!'
text_gym_later = 'OK, через сколько тебе о ней напомнить?'
img_clock = '⏳'

question_text = "День подходит к концу. Уделила ли ты сегодня время спорту?"

reg_text1 = 'Ты молодец! Отдыхай!'
reg_text2 = 'Я понял. Тренировки сегодня не было'

first_time_h, first_time_m = 0, 20  # work at 10:00
second_time_h, second_time_m = 23, 0  # work at 23:00
