import telebot
from telebot import types

# Токен вашего бота
TOKEN = "7635930726:AAGtZJCZNuioKevgOcSciNPj_RYPAZmFvCA"
bot = telebot.TeleBot(TOKEN)

# Обработчик кнопки "Вернуться в главное меню"
@bot.callback_query_handler(func=lambda call: call.data == "back_to_main")
def back_to_main(call):
    markup = create_main_keyboard()  # Создаем клавиатуру для главного меню
    bot.answer_callback_query(call.id)
    bot.edit_message_text("Выберите одну из опций:", chat_id=call.message.chat.id, message_id=call.message.message_id,
                          reply_markup=markup)

# Функция для создания клавиатуры для главного меню
def create_main_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Список документов для поступления", callback_data="documents")
    item2 = types.InlineKeyboardButton("Сроки подачи документов", callback_data="deadlines")
    item3 = types.InlineKeyboardButton("Информация о специальностях", callback_data="specialties")
    item4 = types.InlineKeyboardButton("Сайт техникума", url="https://stotis.sakhalin.gov.ru/")
    item5 = types.InlineKeyboardButton("FAQ", callback_data="faq")
    item6 = types.InlineKeyboardButton("Контакты", callback_data="contacts")
    item7 = types.InlineKeyboardButton("Вступительные экзамены", callback_data="exams")
    item8 = types.InlineKeyboardButton("Контрольные цифры приёма", callback_data="admission_numbers")
    return markup.add(item1, item2, item3, item4, item5, item6, item7, item8)

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

    back_button = types.InlineKeyboardButton("Вернуться в главное меню", callback_data="back_to_main")

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
    back_button = types.InlineKeyboardButton("Вернуться в главное меню", callback_data="back_to_main")
    markup.add(back_button)

    bot.answer_callback_query(call.id)
    bot.edit_message_text(deadlines_info, chat_id=call.message.chat.id, message_id=call.message.message_id,
                          reply_markup=markup)

# Функция для создания клавиатуры для выбора специальностей
def create_specialty_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=3)
    item1 = types.InlineKeyboardButton("1 - 38.02.04 Коммерция (по отраслям)", callback_data="specialty_1")
    item2 = types.InlineKeyboardButton("2 - 43.02.15 Поварское и кондитерское дело", callback_data="specialty_2")
    item3 = types.InlineKeyboardButton("3 - 43.01.09 Повар, кондитер", callback_data="specialty_3")
    item4 = types.InlineKeyboardButton("4 - 38.02.08 Торговое дело", callback_data="specialty_4")
    item5 = types.InlineKeyboardButton("5 - 22.02.06 Сварочное производство", callback_data="specialty_1")
    item6 = types.InlineKeyboardButton("6 - 15.02.19 Сварочное производство", callback_data="specialty_2")
    item7 = types.InlineKeyboardButton("7 - 15.02.10 Мехатроника и мобильная робототехника",
                                       callback_data="specialty_3")
    item8 = types.InlineKeyboardButton("8 - 15.02.10 Мехатроника и робототехника (по отраслям)",
                                       callback_data="specialty_4")
    item9 = types.InlineKeyboardButton("9 - 10.02.05 Организация и технология защиты информации",
                                       callback_data="specialty_1")
    item10 = types.InlineKeyboardButton("10 - 10.02.05 Обеспечение информационной безопасности",
                                        callback_data="specialty_2")
    item11 = types.InlineKeyboardButton("11 - 09.02.07 Информационные системы и программирование",
                                        callback_data="specialty_3")
    item12 = types.InlineKeyboardButton("12 - 15.01.05 Сварщик (ручной и частично механизированной сварки",
                                        callback_data="specialty_4")
    item13 = types.InlineKeyboardButton("13 - 15.01.05 Сварщик (ручной и частично механизированной сварки",
                                        callback_data="specialty_1")
    item14 = types.InlineKeyboardButton(
        "14 - 08.01.26 Мастер по ремонту и обслуживанию инженерных систем ЖКХ 2020-2022",
        callback_data="specialty_2")
    item15 = types.InlineKeyboardButton("15 - 08.01.29 Мастер по ремонту и обслуживанию инженерных систем ЖКХ 2023",
                                        callback_data="specialty_3")
    item16 = types.InlineKeyboardButton(
        "16 - 23.02.07 Техническое обслуживание и ремонт двигателей, систем и агрегатов автомобилей",
        callback_data="specialty_4")
    markup.add(item1, item9)
    markup.add(item2, item10)
    markup.add(item3, item11)
    markup.add(item4, item12)
    markup.add(item5, item13)
    markup.add(item6, item14)
    markup.add(item7, item15)
    markup.add(item8, item16)
    return markup

# Обработчик кнопки "Информация о специальностях"
@bot.callback_query_handler(func=lambda call: call.data == "specialties")
def specialties(call):
    specialties_info = (
        "На текущий год доступны следующие специальности:\n"
        "1. 38.02.04 Коммерция (по отраслям)\n"
        "2. 43.02.15 Поварское и кондитерское дело\n"
        "3. 43.01.09 Повар, кондитер\n"
        "4. 38.02.08 Торговое дело\n"
        "5. 22.02.06 Сварочное производство\n"
        "6. 15.02.19 Сварочное производство\n"
        "7. 15.02.10 Мехатроника и мобильная робототехника\n"
        "8. 15.02.10 Мехатроника и робототехника (по отраслям)\n"
        "9. 10.02.05 Организация и технология защиты информации\n"
        "10. 10.02.05 Обеспечение информационной безопасности\n"
        "11. 09.02.07 Информационные системы и программирование\n"
        "12. 15.01.05 Сварщик (ручной и частично механизированной сварки\n"
        "13. 15.01.05 Сварщик (ручной и частично механизированной сварки\n"
        "14. 08.01.26 Мастер по ремонту и обслуживанию инженерных систем ЖКХ 2020-2022\n"
        "15. 08.01.29 Мастер по ремонту и обслуживанию инженерных систем ЖКХ 2023\n"
        "16. 23.02.07 Техническое обслуживание и ремонт двигателей, систем и агрегатов автомобилей\n"
    )
    markup = create_specialty_keyboard()  # Создаем клавиатуру для выбора специальности
    back_button = types.InlineKeyboardButton("Вернуться в главное меню", callback_data="back_to_main")
    markup.add(back_button)

    bot.answer_callback_query(call.id)
    bot.edit_message_text(specialties_info, chat_id=call.message.chat.id, message_id=call.message.message_id,
                          reply_markup=markup)

# Обработчик выбора специальности
@bot.callback_query_handler(func=lambda call: call.data.startswith("specialty_"))
def specialty_details(call):
    if call.data == "specialty_1":
        details = ("Наименование квалификации базовой подготовки: "
                   "Менеджер по продажам."
                   "Важным звеном торговой деятельности является менеджер по продажам. Эта специальность в современной экономической системе оказалась чрезвычайно популярной и востребованной. За иностранным названием скрыто интересное ремесло, порой граничащее с виртуозным искусством.")
        more_info_button = types.InlineKeyboardButton("Подробнее",
                                                      url="https://stotis.sakhalin.gov.ru/spetsialnosti-i-professii-stotis/kommertsiya-po-otraslyam/")
    elif call.data == "specialty_2":
        details = "Специалист по поварскому и кондитерскому делу – это организатор процесса приготовления блюд, кондитерских изделий сложного ассортимента и квалифицированный повар. Профессии: пекарь, повар, кондитер занимают 29 место в списке наиболее востребованных на рынке труда, новых и перспективных профессий, требующих среднего профессионального образования (приказ Минтруда России и соцзащиты РФ от 30.12.2022 г. №831)."
        more_info_button = types.InlineKeyboardButton("Подробнее",
                                                      url="https://stotis.sakhalin.gov.ru/spetsialnosti-i-professii-stotis/pkd/")
    elif call.data == "specialty_3":
        details = "Профессии: пекарь, повар, кондитер занимают 29 место в списке наиболее востребованных на рынке труда, новых и перспективных профессий, требующих среднего профессионального образования (приказ Минтруда России и соцзащиты РФ от 30.12.2022 г. №831)."
        more_info_button = types.InlineKeyboardButton("Подробнее",
                                                      url="https://stotis.sakhalin.gov.ru/spetsialnosti-i-professii-stotis/pk/pk.php")
    elif call.data == "specialty_4":
        details = "Внимание! Образовательная программа по специальности 38.02.08 \"Торговое дело\" является одной из наиболее востребованных и перспективных в современном бизнесе. Профессиональный путь, связанный с этой областью, предоставляет широкий спектр возможностей для карьерного роста и развития."
        more_info_button = types.InlineKeyboardButton("Подробнее",
                                                      url="https://stotis.sakhalin.gov.ru/spetsialnosti-i-professii-stotis/trading-business/trading-business.php")
    elif call.data == "specialty_5":
        details = (
            "Техник сварочного производства на протяжении десятилетий является одной из стабильно востребованных профессий. "
            "Специалист сварочного производства занимает 56 место в списке наиболее востребованных на рынке труда, новых и перспективных профессий, требующих среднего профессионального образования (приказ Минтруда России и соцзащиты РФ от 30.12.2022 г. №831).")
        more_info_button = types.InlineKeyboardButton("Подробнее",
                                                      url="https://stotis.sakhalin.gov.ru/spetsialnosti-i-professii-stotis/sp/sp.php")
    elif call.data == "specialty_6":
        details = ("Программа реализуется с 2024 года в рамках Федеральной программы \"Профессионалитет\"."
                   "Наименование квалификации базовой подготовки специалиста среднего звена:"
                   "Техник."
                   "Сварочные работы по востребованности находятся на первых семи позициях, а их качественное выполнение гарантирует высокую оплату и возможность карьерного роста."
                   "Специалист сварочного производства занимает 56 место в списке наиболее востребованных на рынке труда, новых и перспективных профессий, требующих среднего профессионального образования (приказ Минтруда России и соцзащиты РФ от 30.12.2022 г. №831).")
        more_info_button = types.InlineKeyboardButton("Подробнее",
                                                      url="https://stotis.sakhalin.gov.ru/spetsialnosti-i-professii-stotis/15-02-19-svarochnoe-proizvodstvo/")
    elif call.data == "specialty_7":
        details = "Специалист по мехатронике и мобильной робототехнике занимает 43 место в списке наиболее востребованных на рынке труда, новых и перспективных профессий, требующих среднего профессионального образования (приказ Минтруда России и соцзащиты РФ от 30.12.2022 г. №831)."
        more_info_button = types.InlineKeyboardButton("Подробнее",
                                                      url="https://stotis.sakhalin.gov.ru/spetsialnosti-i-professii-stotis/mimr/mimr.php")
    elif call.data == "specialty_8":
        details = ("Наименование квалификации специалиста среднего звена:"
                   "Специалист по мехатронике и робототехнике."
                   "Специалист по робототехнике — это высококвалифицированный специалист, который занимается проектированием, разработкой, программированием и обслуживанием роботизированных систем, которые могут выполнять задачи автономно или с помощью человека.")
        more_info_button = types.InlineKeyboardButton("Подробнее",
                                                      url="https://stotis.sakhalin.gov.ru/spetsialnosti-i-professii-stotis/mekhatronika-i-robototekhnika-po-otraslyam/")
    elif call.data == "specialty_9":
        details = (
            "Техник по защите информации это специалист, который занимается обеспечением информационной безопасности предприятия и его информационной инфраструктуры, техническим обслуживанием средств защиты информации."
            "Специалист по информационной безопасности занимает 40 место в списке наиболее востребованных на рынке труда, новых и перспективных профессий, требующих среднего профессионального образования (приказ Минтруда России и соцзащиты РФ от 30.12.2022 г. №831).")
        more_info_button = types.InlineKeyboardButton("Подробнее",
                                                      url="https://stotis.sakhalin.gov.ru/spetsialnosti-i-professii-stotis/otzi1-16/")
    elif call.data == "specialty_10":
        details = "Специалист по информационной безопасности занимает 40 место в списке наиболее востребованных на рынке труда, новых и перспективных профессий, требующих среднего профессионального образования (приказ Минтруда России и соцзащиты РФ от 30.12.2022 г. №831)."
        more_info_button = types.InlineKeyboardButton("Подробнее",
                                                      url="https://stotis.sakhalin.gov.ru/spetsialnosti-i-professii-stotis/oib/oib.php")
    elif call.data == "specialty_11":
        details = (
            "Информационные системы и программирование - на сегодняшний день одна из самых приоритетных специальностей. Квалификация, которая будет получена в результате обучения."
            "Специалист по информационным системам и программированию занимает 41 место в списке наиболее востребованных на рынке труда, новых и перспективных профессий, требующих среднего профессионального образования (приказ Минтруда России и соцзащиты РФ от 30.12.2022 г. №831).")
        more_info_button = types.InlineKeyboardButton("Подробнее",
                                                      url="https://stotis.sakhalin.gov.ru/spetsialnosti-i-professii-stotis/isip/isip.php")
    elif call.data == "specialty_12":
        details = "Сварщик – специалист по металлу, который соединяет металлические детали в сложные конструкции при помощи электрической или газовой сварки. Профессия сварщик занимает 56 место в списке наиболее востребованных на рынке труда, новых и перспективных профессий, требующих среднего профессионального образования (приказ Минтруда России и соцзащиты РФ от 30.12.2022 г. №831)."
        more_info_button = types.InlineKeyboardButton("Подробнее",
                                                      url="https://stotis.sakhalin.gov.ru/spetsialnosti-i-professii-stotis/sv/sv.php")
    elif call.data == "specialty_13":
        details = ("Квалификация квалифицированного рабочего, служащего:  "
                   "сварщик."
                   "Сварщик – специалист по металлу, который соединяет металлические детали в сложные конструкции при помощи электрической или газовой сварки. Профессия сварщик занимает 56 место в списке наиболее востребованных на рынке труда, новых и перспективных профессий, требующих среднего профессионального образования (приказ Минтруда России и соцзащиты РФ от 30.12.2022 г. №831).")
        more_info_button = types.InlineKeyboardButton("Подробнее",
                                                      url="https://stotis.sakhalin.gov.ru/spetsialnosti-i-professii-stotis/15-01-05-svarshchik-elektrosvarochnye-i-gazosvarochnye-raboty/")
    elif call.data == "specialty_14":
        details = "Мастер по ремонту и обслуживанию инженерных систем ЖКХ - это специалист-универсал широкого профиля, занимающийся организацией эксплуатации зданий, сооружений, конструкций, оборудования систем водоснабжения, водоотведения, отопления и осветительных сетей ЖКХ и их ремонтом."
        more_info_button = types.InlineKeyboardButton("Подробнее",
                                                      url="https://stotis.sakhalin.gov.ru/spetsialnosti-i-professii-stotis/mrois/mrois.php")
    elif call.data == "specialty_15":
        details = "Мастер по ремонту и обслуживанию инженерных систем ЖКХ - это специалист-универсал широкого профиля, занимающийся организацией ремонта, монтажа и эксплуатацией оборудования систем водоснабжения, водоотведения, отопления и осветительных сетей ЖКХ."
        more_info_button = types.InlineKeyboardButton("Подробнее",
                                                      url="https://stotis.sakhalin.gov.ru/spetsialnosti-i-professii-stotis/mrois2023/")
    elif call.data == "specialty_16":
        details = "Техническое обслуживание и ремонт двигателей и агрегатов автомобилей – специальность, выпускник которой владеет навыками не только грамотной эксплуатации автомобилей, но и может организовывать технологические процессы обслуживания и ремонта. Мастер по ремонту и обслуживанию автомобилей занимает 16 место в списке наиболее востребованных на рынке труда, новых и перспективных профессий, требующих среднего профессионального образования (приказ Минтруда России и соцзащиты РФ от 30.12.2022 г. №831)."
        more_info_button = types.InlineKeyboardButton("Подробнее",
                                                      url="https://stotis.sakhalin.gov.ru/spetsialnosti-i-professii-stotis/tord/tord.php")

    markup = types.InlineKeyboardMarkup(row_width=1)
    back_button = types.InlineKeyboardButton("Вернуться к списку специальностей",
                                             callback_data="back_to_specialties")
    markup.add(more_info_button, back_button)

    bot.answer_callback_query(call.id)
    bot.edit_message_text(details, chat_id=call.message.chat.id, message_id=call.message.message_id,
                          reply_markup=markup)

# Обработчик кнопки "Вернуться к списку специальностей"
@bot.callback_query_handler(func=lambda call: call.data == "back_to_specialties")
def back_to_specialties(call):
    specialties_info = (
        "На текущий год доступны следующие специальности:\n"
        "1. 38.02.04 Коммерция (по отраслям)\n"
        "2. 43.02.15 Поварское и кондитерское дело\n"
        "3. 43.01.09 Повар, кондитер\n"
        "4. 38.02.08 Торговое дело\n"
        "5. 22.02.06 Сварочное производство\n"
        "6. 15.02.19 Сварочное производство\n"
        "7. 15.02.10 Мехатроника и мобильная робототехника\n"
        "8. 15.02.10 Мехатроника и робототехника (по отраслям)\n"
        "9. 10.02.05 Организация и технология защиты информации\n"
        "10. 10.02.05 Обеспечение информационной безопасности\n"
        "11. 09.02.07 Информационные системы и программирование\n"
        "12. 15.01.05 Сварщик (ручной и частично механизированной сварки\n"
        "13. 15.01.05 Сварщик (ручной и частично механизированной сварки\n"
        "14. 08.01.26 Мастер по ремонту и обслуживанию инженерных\n"
        "15. 08.01.29 Мастер по ремонту и обслуживанию инженерных\n"
        "16. 23.02.07 Техническое обслуживание и ремонт двигателей, систем и агрегатов автомобилей\n"
    )
    markup = create_specialty_keyboard()  # Пересоздаем клавиатуру для выбора специальности
    back_button = types.InlineKeyboardButton("Вернуться в главное меню", callback_data="back_to_main")
    markup.add(back_button)

    bot.answer_callback_query(call.id)
    bot.edit_message_text(specialties_info, chat_id=call.message.chat.id, message_id=call.message.message_id,
                          reply_markup=markup)

# Обработчик кнопки "FAQ"
@bot.callback_query_handler(func=lambda call: call.data == "faq")
def faq(call):
    faq_text = (
        "FAQ:\n\n"
        "<b>1. Как подать документы?</b>\nОтвет: Для подачи документов заполните онлайн-форму на сайте техникума.\n\n"
        "<b>2. Какие документы нужны для поступления?</b>\nОтвет: Для поступления необходимы паспорт, аттестат, фото и медицинская справка.\n\n"
        "<b>3. Когда начинаются вступительные экзамены?</b>\nОтвет: Экзамены начинаются с 1 июля."
    )
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_button = types.InlineKeyboardButton("Вернуться в главное меню", callback_data="main")
    markup.add(back_button)

    bot.answer_callback_query(call.id)
    bot.edit_message_text(faq_text, chat_id=call.message.chat.id, message_id=call.message.message_id,
                          reply_markup=markup, parse_mode="HTML")

# Обработчик кнопки "Контакты"
@bot.callback_query_handler(func=lambda call: call.data == "contacts")
def contacts(call):
    contact_info = (
        "Контакты:\n\n"
        "Телефон: 8 (42433) 2-09-82, 5-26-81\n"
        "Факс: 8 (42433)-66-401\n"
        "E-mail: stotis@sakhalin.gov.ru\n"
        "Адрес: Сахалинская область, г. Холмск, ул. Победы, 10"
    )
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_button = types.InlineKeyboardButton("Вернуться в главное меню", callback_data="main")
    markup.add(back_button)

    bot.answer_callback_query(call.id)
    bot.edit_message_text(contact_info, chat_id=call.message.chat.id, message_id=call.message.message_id,
                          reply_markup=markup)

# Обработчик кнопки "Вступительные экзамены"
@bot.callback_query_handler(func=lambda call: call.data == "exams")
def exams(call):
    exams_info = (
        "<b>Зачисление проводится без вступительных испытаний</b> \n\n"
        "В случае,  если численность поступающих  превышает количество мест, будет проводиться отбор  по конкурсу аттестатов, на основе результатов освоения поступающими образовательной программы основного общего образования, указанных в представленных поступающими документах об образовании."
    )
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_button = types.InlineKeyboardButton("Вернуться в главное меню", callback_data="back_to_main")
    markup.add(back_button)

    bot.answer_callback_query(call.id)
    bot.edit_message_text(exams_info, chat_id=call.message.chat.id, message_id=call.message.message_id,
                          reply_markup=markup, parse_mode="HTML")


# Обработчик кнопки "Контрольные цифры приёма"
@bot.callback_query_handler(func=lambda call: call.data == "admission_numbers")
def admission_numbers(call):
    # Отправка изображения с таблицей
    bot.send_photo(call.message.chat.id, open("files/Контрольные цифры приёма.png", 'rb'))

    markup = types.InlineKeyboardMarkup(row_width=1)
    back_button = types.InlineKeyboardButton("Вернуться в главное меню", callback_data="back_to_main")
    markup.add(back_button)

    bot.answer_callback_query(call.id)
    bot.edit_message_text("Таблица с контрольными цифрами приёма:", chat_id=call.message.chat.id, message_id=call.message.message_id,
                          reply_markup=markup)

# Запуск бота
bot.polling(none_stop=True)



