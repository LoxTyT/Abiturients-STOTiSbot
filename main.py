import telebot
from telebot import types

# Токен вашего бота
TOKEN = "7635930726:AAGtZJCZNuioKevgOcSciNPj_RYPAZmFvCA"
bot = telebot.TeleBot(TOKEN)

# Список всех доступных команд
valid_commands = ['/start', '/help', '/info', '/faq', '/contacts']

# Функция для создания клавиатуры для главного меню
def create_main_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Список документов для поступления", callback_data="documents")
    item2 = types.InlineKeyboardButton("Сроки подачи документов", callback_data="deadlines")
    return markup.add(item1, item2,)

# Обработчик для сообщений, не являющихся командами
@bot.message_handler(func=lambda message: not message.text.startswith('/'))
def handle_non_command(message):
    bot.reply_to(message, "Извините, я не понимаю ваш запрос. Пожалуйста, используйте команду /help для получения информации о доступных командах.")

# Обработчик для команд, которые не являются валидными
@bot.message_handler(func=lambda message: message.text.startswith('/') and message.text not in valid_commands)
def handle_invalid_command(message):
    bot.reply_to(message, "Извините, я не понимаю ваш запрос. Пожалуйста, используйте команду /help для получения информации о доступных командах.")

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

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def help(message):
    help_text = (
        "Доступные команды и кнопки:\n\n"
        "/start - Начать работу с ботом.\n"
        "/help - Вывести информацию о командах и кнопках.\n"
        "/info - Информация о техникуме\n"
        "/faq - Часто задаваемые вопросы.\n"
        "/contacts - Контактная информация.\n\n"
        "Доступные кнопки:\n\n"
        "1. <b>Список документов для поступления</b> - Получить информацию о документах для поступления.\n"
        "2. <b>Сроки подачи документов</b> - Узнать сроки подачи документов.\n"
        "3. <b>Информация о специальностях</b> - Получить информацию о доступных специальностях.\n"
        "4. <b>Сайт техникума</b> - Перейти на официальный сайт техникума.\n"
        "5. <b>FAQ</b> - Часто задаваемые вопросы.\n"
        "6. <b>Контакты</b> - Получить контактную информацию техникума.\n"
        "7. <b>Вступительные экзамены</b> - Узнать информацию о вступительных экзаменах.\n"
        "8. <b>Контрольные цифры приёма</b> - Посмотреть таблицу контрольных цифр приёма.\n"
        "9. <b>Информация об общежитии</b> - Получить информацию об общежитии.\n"
        "10. <b>Онлайн приём</b> - Перейти на страницу для подачи онлайн-заявки.\n"
        "11. <b>Правила приёма</b> - Ознакомиться с правилами приёма в техникум.\n"
        "\nКаждая кнопка соответствует одной из опций, доступных в главном меню."
    )

    # Отправляем сообщение с помощью бота
    bot.send_message(message.chat.id, help_text, parse_mode="HTML")

# Команда /info - информация о техникуме
@bot.message_handler(commands=['info'])
def info(message):
    info_text = (
        "ГБПОУ «Сахалинский техникум отраслевых технологий и сервиса» — это учебное заведение, "
        "предоставляющее образование по программам среднего профессионального образования. Мы готовим специалистов "
        "по таким направлениям как коммерция, поварское и кондитерское дело, мехатроника и другие.\n\n"
        "Мы гордимся высокой квалификацией наших преподавателей и современным оснащением учебных кабинетов и лабораторий. "
        "Техникум готовит специалистов, которые востребованы на рынке труда, и предоставляет студентам все необходимые "
        "ресурсы для успешной учебы и дальнейшей карьеры."
    )
    bot.send_message(message.chat.id, info_text)

# Команда /faq - часто задаваемые вопросы
@bot.message_handler(commands=['faq'])
def faq(message):
    faq_text = (
        "FAQ:\n\n"
        "<b>1. Как подать документы?</b>\nОтвет: Для подачи документов заполните онлайн-форму на сайте техникума.\n\n"
        "<b>2. Какие документы нужны для поступления?</b>\nОтвет: Для поступления необходимы паспорт, аттестат, фото и медицинская справка.\n\n"
        "<b>3. Когда начинаются вступительные экзамены?</b>\nОтвет: Экзамены начинаются с 1 июля."
    )
    bot.send_message(message.chat.id, faq_text, parse_mode="HTML")

# Команда /contacts - контактная информация
@bot.message_handler(commands=['contacts'])
def contacts(message):
    contacts_text = (
        "Контактная информация:\n\n"
        "Телефон: 8 (42433) 2-09-82, 5-26-81\n"
        "Факс: 8 (42433)-66-401\n"
        "E-mail: stotis@sakhalin.gov.ru\n"
        "Адрес: Сахалинская область, г. Холмск, ул. Победы, 10"
    )
    bot.send_message(message.chat.id, contacts_text)

# Обработчик кнопки "Список документов для поступления"
@bot.callback_query_handler(func=lambda call: call.data == "documents")
def documents(call):
    doc_list = [
        "При подаче заявления о приеме в ГБПОУ «Сахалинский техникум отраслевых технологий и сервиса» поступающий предъявляет следующие документы:\n\n"
        "1. Заявление;",
        "2. Документ об образовании (подлинник и копия: документа и вкладыша);",
        "3. Паспорт (оригинал и копия паспорта);",
        "4. ИНН (копия);",
        "5. СНИЛС (копия)",
        "6. Медицинская комиссия (форма 086-У)",
        "7. Фотографии 3х4 см — 4 штук",
        "8. Приписное свидетельство (для парней, если нет приписного свидетельства, тогда характеристика из школы)",
        "9. Полис обязательного медицинского страхования",
        "Приемная комиссия работает в Учебной части, кабинет № 108 учебного корпуса ГБПОУ «СТОТиС»\n\n",
        "Для детей-сирот и детей, оставшихся без попечения родителей, к выше перечисленным документам дополнительно требуется:\n",
        "1. Свидетельство о рождении ребёнка и свидетельство о заключении брака (при наличии соответствующих документов), копии свидетельств.",
        "2. Свидетельство о смерти родителей (если они умерли).",
        "3. Решение суда о лишении или ограничении родительских прав, о признании родителей безвестно отсутствующими, недееспособными (ограниченно дееспособными), отбывании ими наказания в местах лишения свободы и другие документы и их копии.",
        "4. Справка из отдела опеки и попечительства о категории детей-сирот и детей, оставшихся без попечения родителей.",
        "5. Решение суда о передачи ребенка опекуну или приемным родителям.",
        "6. Справка, подтверждающая опекунство (и где ребенок будет проживать).",
        "7. Копия анкеты ребёнка, анкеты выпускника областного государственного образовательного учреждения.",
        "8. Документ о закреплении жилья или о постановке ребенка на льготную очередь на получение жилья (выдает администрация МО по месту рождения или прописки).",
    ]

    # Создаем клавиатуру с кнопками для файлов
    markup = types.InlineKeyboardMarkup(row_width=1)

    file_button_1 = types.InlineKeyboardButton("Образец заявления на место в общежитии",
                                               callback_data="obrazec_obchejitie")
    file_button_2 = types.InlineKeyboardButton("Образец заявления на обучение по программам СПО (заочное)",
                                               callback_data="zayavlenie_zaochnoe")
    file_button_3 = types.InlineKeyboardButton("Образец заявления на обучение по программам СПО (очное)",
                                               callback_data="zayavlenie_ochnoe")

    back_button = types.InlineKeyboardButton("Вернуться в главное меню", callback_data="main")

    markup.add(file_button_1, file_button_2, file_button_3, back_button)

    bot.answer_callback_query(call.id)
    bot.edit_message_text("\n".join(doc_list), chat_id=call.message.chat.id, message_id=call.message.message_id,
                          reply_markup=markup)


# Обработчик для отправки файлов по кнопкам
@bot.callback_query_handler(func=lambda call: call.data == "obrazec_obchejitie")
def send_file_1(call):
    file_path = "files/Образец заявления на место в общежитии.pdf"  # Укажите путь к вашему файлу
    bot.send_document(call.message.chat.id, open(file_path, 'rb'))
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data == "zayavlenie_zaochnoe")
def send_file_2(call):
    file_path = "files/Образец заявления на обучение по программам СПО (заочное).pdf"  # Укажите путь к вашему файлу
    bot.send_document(call.message.chat.id, open(file_path, 'rb'))
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data == "zayavlenie_ochnoe")
def send_file_3(call):
    file_path = "files/Образец заявления на обучение по программам СПО (очное).pdf"  # Укажите путь к вашему файлу
    bot.send_document(call.message.chat.id, open(file_path, 'rb'))
    bot.answer_callback_query(call.id)


# Обработчик кнопки "Сроки подачи документов"
@bot.callback_query_handler(func=lambda call: call.data == "deadlines")
def deadlines(call):
    deadlines_info = "Сроки подачи документов: с 1 апреля по 15 июля."
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_button = types.InlineKeyboardButton("Вернуться в главное меню", callback_data="main")
    markup.add(back_button)

    bot.answer_callback_query(call.id)
    bot.edit_message_text(deadlines_info, chat_id=call.message.chat.id, message_id=call.message.message_id,
                          reply_markup=markup)

# Запуск бота
bot.polling(none_stop=True)



