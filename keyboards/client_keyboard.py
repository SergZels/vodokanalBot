from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


b1 = KeyboardButton("/Подати_показник")

kbcl = ReplyKeyboardMarkup(resize_keyboard=True)
kbcl.add(b1)