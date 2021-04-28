from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


inline_key = InlineKeyboardMarkup()
btn = InlineKeyboardButton('да', callback_data='yes')
btn1 = InlineKeyboardButton('нет', callback_data='no')

inline_key.add(btn, btn1)