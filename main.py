import telebot
from telebot import types

# Токен вашего бота
TOKEN = "7635930726:AAGtZJCZNuioKevgOcSciNPj_RYPAZmFvCA"
bot = telebot.TeleBot(TOKEN)

# Функция для создания клавиатуры для главного меню
def create_main_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Список документов для поступления", callback_data="documents")
    item2 = types.InlineKeyboardButton("Сроки подачи документов", callback_data="deadlines")
    return markup.add(item1, item2,)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    # Получаем имя и фамилию пользователя
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    # Приветственное сообщение с именем и фамилией пользователя
    welcome_text = f"Привет, {first_name} {last_name}!\nДобро пожаловать в бот 'Помощь Абитуриентам СТОТиС'!\nЯ помогу вам с информацией о поступлении в техникум."

    # Создаем клавиатуру
    markup = create_main_keyboard()

    # Отправляем приветствие и клавиатуру в одном сообщении
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

# Запуск бота
bot.polling(none_stop=True)



