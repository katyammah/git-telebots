import os
import random
import sqlite3
import time
from threading import Thread

import schedule
import telebot
from dotenv import find_dotenv, load_dotenv
from telebot import types

import constants as cs
import queries
from constants import chat_id
from utils import calc_dates

con = sqlite3.connect('database2.db', check_same_thread=False)
cur = con.cursor()

queries.create_table(month=cs.month_name)

load_dotenv(find_dotenv())
token = os.getenv('TOKEN')
bot = telebot.TeleBot(token)

btn = types.InlineKeyboardMarkup(row_width=1)
btn1 = types.InlineKeyboardButton(text=cs.btn1_text, url=random.choice(cs.wrkout1))
btn2 = types.InlineKeyboardButton(text=cs.btn2_text, url=random.choice(cs.wrkout2))
btn3 = types.InlineKeyboardButton(text=cs.btn3_text, url=random.choice(cs.wrkout3))
btn.add(btn1, btn2, btn3)

btntime = types.InlineKeyboardMarkup(row_width=2)
btn4 = types.InlineKeyboardButton(text='⏰ 15 минут', callback_data='15 min')
btn5 = types.InlineKeyboardButton(text='⏰ 1 час', callback_data='1 hour')
btn6 = types.InlineKeyboardButton(text='⏰ 2 часа', callback_data='2 hour')
btn7 = types.InlineKeyboardButton(text='🙈 Завтра', callback_data='tomorrow')
btntime.add(btn4, btn5, btn6, btn7)

buttons = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton(text='Сейчас', callback_data='now')
button2 = types.InlineKeyboardButton(text='Позже', callback_data='later')
buttons.add(button1, button2)


def start():
    bot.send_message(chat_id=chat_id, text=cs.hello_text,
                     reply_markup=buttons)


def end_of_day():
    endbuttons = types.ReplyKeyboardMarkup(True, True)
    endbuttons.row('Да', 'Нет')
    msg = bot.send_message(chat_id=chat_id, text=cs.question_text,
                           reply_markup=endbuttons)
    bot.register_next_step_handler(msg, reg)


@bot.message_handler(content_types=['text'])
def reg(message):  # adding data about today's workout to datebase

    num_id = queries.get_num_id(month=cs.month_name)
    date_now = cs.my_now.strftime('%d %B (%A)')

    if message.text == 'Да':
        bot.send_message(message.chat.id, text=cs.reg_text1)
        wrk = "Выполнена"
        queries.db_data_add(month=cs.month_name, id=num_id, workout_ex=wrk, date=date_now)

    if message.text == 'Нет':
        bot.send_message(message.chat.id, text=cs.reg_text2)
        wrk = "Не выполнена"
        queries.db_data_add(month=cs.month_name, id=num_id, workout_ex=wrk, date=date_now)


def answer(call):
    if call.data == 'now':
        bot.send_message(call.message.chat.id, text=cs.text_ready_gym_now, reply_markup=btn)

    if call.data == 'later':
        bot.send_message(call.message.chat.id, text=cs.text_gym_later, reply_markup=btntime)

    if call.data == '15 min':
        bot.send_message(call.message.chat.id, text='ОК, напомню через 15 минут!')
        time.sleep(1)
        bot.send_message(call.message.chat.id, text=cs.img_clock)
        time.sleep(60 * 15)
        bot.send_message(call.message.chat.id, text='15 минут прошло!', reply_markup=btn)

    if call.data == '1 hour':
        bot.send_message(call.message.chat.id, text='ОК, напомню через час!')
        time.sleep(1)
        bot.send_message(call.message.chat.id, text=cs.img_clock)
        time.sleep(60 * 60)
        bot.send_message(call.message.chat.id, text='1 час прошёл!', reply_markup=btn)

    if call.data == '2 hour':
        bot.send_message(call.message.chat.id, text='ОК, напомню через 2 часа!')
        time.sleep(1)
        bot.send_message(call.message.chat.id, text=cs.img_clock)
        time.sleep(2 * 60 * 60)
        bot.send_message(call.message.chat.id, text='2 часа прошло!', reply_markup=btn)

    if call.data == 'tomorrow':
        bot.send_message(call.message.chat.id, text=cs.text_to_tomorrow)
        time.sleep(1)
        bot.send_message(call.message.chat.id, text=cs.img_clock)
        time.sleep(24 * 60 * 60)
        bot.send_message(call.message.chat.id, text=cs.text_tomorrow_start, reply_markup=buttons)


def do_schedule():
    first_remind_at, second_remind_at = calc_dates()
    schedule.every().monday.at(first_remind_at).do(start)
    schedule.every().wednesday.at(first_remind_at).do(start)
    schedule.every().saturday.at(first_remind_at).do(start)
    #   schedule.every().day.at(cs.first_remind_at).do(start)  # uncomment for checking code

    schedule.every().day.at(second_remind_at).do(end_of_day)

    while True:
        schedule.run_pending()
        time.sleep(1)


def main_loop():
    thread = Thread(target=do_schedule)
    thread.start()
    bot.polling(True)


if __name__ == '__main__':
    main_loop()
