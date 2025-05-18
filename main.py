import telebot
from telebot import types

# Токен вашего бота
TOKEN = "7635930726:AAEW76cfOKMWKroU512IFYNCp8keWM1qgq4"
bot = telebot.TeleBot(TOKEN)

# Запуск бота
bot.polling(none_stop=True)



