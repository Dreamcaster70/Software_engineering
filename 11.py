import time
import threading
import telebot
from telebot import types
import datetime

TOKEN = 'Токен сюда'

bot = telebot.TeleBot(TOKEN)

# словарь с пользователями
users = {}


# отправляет напоминания
def send_reminder(user_id, interval):
    while True:
        try:
            threading.Event().wait(interval) # выдерживает интервал перед напоминаниями
            bot.send_message(user_id, "Пора поменять линзы!")
            users[user_id]['last_change_date'] = datetime.datetime.now().date() # обновляет время

        except Exception as ex:
            print(f"Ошибка отправки напоминания: {ex}")



@bot.message_handler(commands=['start']) # /start
def handle_start(message):
    user_id = message.from_user.id # добываем уникальный user id из сообщения
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # это нужно чтоб добавить кнопки
    btn1 = types.KeyboardButton('/set_interval')
    btn2 = types.KeyboardButton('/time_left') # кнопки
    btn3 = types.KeyboardButton('/interval')
    markup.add(btn1)
    markup.add(btn2) # добавить кнопки на экран
    markup.add(btn3)
    users[user_id] = {'last_change_date': datetime.date.today()} # добавляем пользователя в словарь
    bot.send_message(user_id, 'Привет! Я бот, который напомнит тебе поменять линзы!')
    time.sleep(1)
    bot.send_message(user_id, 'Чтобы изменить интервал введите /set_interval , чтобы посмотреть оставшееся время до замены введите /time_left, чтобы посмотреть установленный интервал введите /interval', reply_markup=markup)

# Обработчик команды /set_interval
@bot.message_handler(commands=['set_interval'])
def set_interval(message):
    user_id = message.from_user.id
    msg = bot.send_message(user_id, "Введите количество дней через которое нужно менять линзы:")
    bot.register_next_step_handler(msg, process_interval_step) # переходим к следующей функции, режим ожидания


def process_interval_step(message):
    user_id = message.from_user.id
    try:
        interval = int(message.text)*86400 # ввод интервала. Тут поменять чтоб проверить
        users[user_id]['interval'] = interval # в словарь добавляется интервал

        # Запуск потока для отправки напоминаний
        threading.Thread(target=send_reminder, args=(user_id, interval)).start()

        bot.send_message(user_id, f"Отлично! Теперь я буду напоминать вам менять линзы каждые {int(interval/86400)} дней.")
    except ValueError:
        bot.send_message(user_id, "Введены неправильные данные, пожалуйста, введите число.")
""" так и не получилось сделать(
@bot.message_handler(commands=['time_left'])
def time_left(user_id):
    if user_id in users and 'interval' in users[user_id]:
        last_change = users[user_id]['last_change_date']
        interval = users[user_id]['interval']
        current_date = datetime.datetime.now().date() 
        days_passed = (current_date - last_change)
        days_left = interval - days_passed
        bot.send_message(user_id, f'До замены осталось {days_left} дней')
"""

@bot.message_handler(commands=['interval'])
def show_interval(message):
    user_id = message.from_user.id
    if user_id in users and 'interval' in users[user_id]: # проверка заполнения словаря
        interval = users[user_id]['interval']
        bot.send_message(user_id, f'Установлен интервал в {int(interval/86400)} дней')
    else:
        bot.send_message(user_id, 'Интервал не установлен. Используйте /set_interval, чтобы установить интервал')

# Запуск бота
bot.polling()