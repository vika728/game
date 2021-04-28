import telebot
from decouple import config
from keyboards.inline_keyboard import inline_key as in_key
import random

bot = telebot.TeleBot(config('TOKEN'))

@bot.message_handler(commands=['game', ])
def welcome(message):
    msg = bot.send_message(message.chat.id, 'Хэй')
    start(msg)

def start(message):
    msg = bot.send_message(message.chat.id, 'Хочешь сыграть в угадайчисло? ', reply_markup=in_key)
    # bot.register_next_step_handler(msg, send_nik)


# def send_nik(message):
#     msg = bot.send_message(message.chat.id, 'Введите ваш ник: ')
#     bot.register_next_step_handler(msg, send_age)


# def send_age(message):
#     bot.send_message(message.chat.id, 'Введите ваш возраст: ')


@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.data == "yes":
        msg = bot.send_message(call.message.chat.id, 'напиши число от от 1 до 100, одно из них я загадала')
        bot.register_next_step_handler(msg, play)
    elif call.data == "no":
        bot.send_message(call.message.chat.id, "okey, в следующий раз тогда")

def play(message):
    number = int(random.randint(1, 101))
    tries = 7
    def func(message):
        response = int(message.text)
        nonlocal tries
        if response == number:
            bot.send_message(message.chat.id, 'Ты угадал')
            tries -= 1
            bot.send_message(message.chat.id, f'У тебя это заняло {7 - tries} попыток')
            start(message)
        elif response > number:
            bot.send_message(message.chat.id, 'Загаданное число поменьше')
            tries -= 1
            msg = bot.send_message(message.chat.id, f'У тебя это отсалось {tries} попыток')
            bot.register_next_step_handler(msg, func)
        elif response < number:
            bot.send_message(message.chat.id, 'Загаданное число побольше')
            msg = bot.send_message(message.chat.id, f'У тебя это осталось {tries} попыток')
            tries-= 1
            bot.register_next_step_handler(msg, func)

        elif tries == 0:
            bot.send_message(message.chat.id, 'Кончились попытки :(')
            start(message)
    func(message)
           

bot.polling(none_stop=True)