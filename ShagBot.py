import telebot
import pyqrcode
from telebot import types

bot = telebot.TeleBot('1107170969:AAEcKoxUynG08lbnHFajPWu9gcw_pXZMUg8')

# ----------------------------------------------------------Кнопки языка при старте----------------------------------------------------------
btnLanguage = telebot.types.ReplyKeyboardMarkup()
btnLanguage.row('Русский')
btnLanguage.row('English')

# ----------------------------------------------------------Старт----------------------------------------------------------
@bot.message_handler(commands=['start', 'старт'])
def start_message(message):
    bot.send_message(message.chat.id, 'Выберите язык / Select language', reply_markup=btnLanguage)

# ----------------------------------------------------------Возврат в начало----------------------------------------------------------
@bot.message_handler(func=lambda message: message.text.lower() == '<Возврат в начало>'.lower() or message.text.lower() == '<Return to start>'.lower())
def btn_login_ru(message):
    start_message(message)

# ----------------------------------------------------------Возврат назад----------------------------------------------------------
@bot.message_handler(func=lambda message: message.text.lower() == '<назад>'.lower() or message.text.lower() == '<back>'.lower())
def btn_back(message):
    btn_welcome(message)


# ----------------------------------------------------------Справочник языка----------------------------------------------------------
dictMsg = {
    'en': {
        'Забыл логин': 'Forget login',
        'Забыл пароль': 'Forget password',
        'Введите пароль': 'Enter password',
        'Welcome': 'Welcome',
        '<Возврат в начало>': '<Return to start>',
        'Ученик': 'Student',
        'Родитель': 'Parent',
        'Средний балл': 'Average score',
        'Посещаемость': 'Attendance',
        'Мероприятия': 'Events',
        'Стоимость обучения': 'Cost training',
        'Конец обучения': 'The end of the training',
        'Отзывы преподавателей': 'Teachers feedback',
        'Когда пара?': 'When pairs?',
        'Где пара?': 'Where pairs?',
        '<Назад>': '<Back>'
    },
    'ru': {
        'Забыл логин': 'Забыл логин',
        'Забыл пароль': 'Забыл пароль',
        'Введите пароль': 'Введите пароль',
        'Welcome': 'Добро пожаловать!',
        '<Возврат в начало>': '<Возврат в начало>',
        'Ученик': 'Ученик',
        'Родитель': 'Родитель',
        'Средний балл': 'Средний балл',
        'Посещаемость': 'Посещаемость',
        'Мероприятия': 'Мероприятия',
        'Стоимость обучения': 'Стоимость обучения',
        'Конец обучения': 'Конец обучения',
        'Отзывы преподавателей': 'Отзывы преподавателей',
        'Когда пара?': 'Когда пара?',
        'Где пара?': 'Где пара?',
        '<Назад>': '<Назад>'
    }
}


# флаг языка
lang = 'en'
# флаг что мы ожидаем авторизацию
awaitAuth = 0
# login user
uLogin = ''
# password user
uPsswd = ''


######
# все функции   начинающиеся с btn_ - выводят кнопки
#               начинающиеся c save_ - сохраняют введенные пользователем данные

# ----------------------------------------------------------Авторизация на русском----------------------------------------------------------
@bot.message_handler(func=lambda message: message.text.lower() == 'русский')
def btn_login_ru(message):
    global awaitAuth, lang
    awaitAuth = 1
    lang = 'ru'
    k = telebot.types.ReplyKeyboardMarkup()
    k.row('Забыл логин')
    k.row('<Возврат в начало>')
    bot.send_message(message.chat.id, 'Введите ваш логин:', reply_markup=k)


# ----------------------------------------------------------Авторизация на английском----------------------------------------------------------
@bot.message_handler(func=lambda message: message.text.lower() == 'english')
def btn_login_en(message):
    global awaitAuth, lang
    awaitAuth = 1
    lang = 'en'
    k = telebot.types.ReplyKeyboardMarkup()
    k.row('Forget login')
    k.row('<Return to start>')
    bot.send_message(message.chat.id, 'Enter login:', reply_markup=k)


# ----------------------------------------------------------Сохранение логина----------------------------------------------------------
@bot.message_handler(func=lambda message: message.content_type == 'text' and awaitAuth == 1)
def save_user_login(message):
    global uLogin, lang, awaitAuth
    awaitAuth = 2
    uLogin = message.text
    k = telebot.types.ReplyKeyboardMarkup()
    k.row('Забыл пароль')
    k.row('<Возврат в начало>')
    bot.send_message(message.chat.id, dictMsg[lang]['Введите пароль'])


# ----------------------------------------------------------Сохранение пароля----------------------------------------------------------
@bot.message_handler(func=lambda message: message.content_type == 'text' and awaitAuth == 2)
def save_user_passwd(message):
    global uLogin, uPsswd, lang, awaitAuth
    awaitAuth = 0
    uPsswd = message.text
    if uLogin == 'admin1' and uPsswd == 'admin2':
        btn_welcome(message)
    else:
        bot.send_message(message.chat.id, 'Oops!')
        if lang == 'ru':
            btn_login_ru(message)
        else:
            btn_login_en(message)

# ----------------------------------------------------------Ученик / Родитель----------------------------------------------------------
def btn_welcome(message):
    k = telebot.types.ReplyKeyboardMarkup()
    k.row(dictMsg[lang]['Ученик'])
    k.row(dictMsg[lang]['Родитель'])
    k.row(dictMsg[lang]['<Возврат в начало>'])
    bot.send_message(message.chat.id, dictMsg[lang]['Welcome'], reply_markup=k)


# ----------------------------------------------------------Панель ученика----------------------------------------------------------
@bot.message_handler(func=lambda message: message.text.lower() == 'ученик' or message.text.lower() == 'student')
def student_panel(message):
    k = telebot.types.ReplyKeyboardMarkup()
    k.row(dictMsg[lang]['Средний балл'], dictMsg[lang]['Посещаемость'], dictMsg[lang]['Мероприятия'])
    k.row(dictMsg[lang]['Конец обучения'], dictMsg[lang]['Отзывы преподавателей'])
    k.row(dictMsg[lang]['<Назад>'])
    if lang == 'ru':
        bot.send_message(message.chat.id, 'Что вы хотите узнать?', reply_markup=k)
    else:
        bot.send_message(message.chat.id, 'What do you want to know?', reply_markup=k)


# ----------------------------------------------------------Панель родителя----------------------------------------------------------
@bot.message_handler(func=lambda message: message.text.lower() == 'родитель' or message.text.lower() == 'parent')
def parent_panel(message):
    k = telebot.types.ReplyKeyboardMarkup()
    k = telebot.types.ReplyKeyboardMarkup()
    k.row(dictMsg[lang]['Средний балл'], dictMsg[lang]['Посещаемость'], dictMsg[lang]['Стоимость обучения'])
    k.row(dictMsg[lang]['Конец обучения'], dictMsg[lang]['Отзывы преподавателей'], dictMsg[lang]['Мероприятия'])
    k.row(dictMsg[lang]['<Назад>'])
    if lang == 'ru':
        bot.send_message(message.chat.id, 'Что вы хотите узнать?', reply_markup=k)
    else:
        bot.send_message(message.chat.id, 'What do you want to know?', reply_markup=k)


# ----------------------------------------------------------Средний балл----------------------------------------------------------
@bot.message_handler(func=lambda message: message.text.lower() == 'средний балл' or message.text.lower() == 'average score')
def average_score(message):
    if lang == 'ru':
        bot.send_message(message.chat.id, 'Ваш средний балл: 11')
    else:
        bot.send_message(message.chat.id, 'Your average score: 11')


# ----------------------------------------------------------Посещаемость----------------------------------------------------------
@bot.message_handler(func=lambda message: message.text.lower() == 'посещаемость' or message.text.lower() == 'attendance')
def attendance(message):
    if lang == 'ru':
        bot.send_message(message.chat.id, 'Ваша посещаемость: 100%')
    else:
        bot.send_message(message.chat.id, 'Your attendance: 100%')


# ----------------------------------------------------------Мероприятия----------------------------------------------------------
@bot.message_handler(func=lambda message: message.text.lower() == 'мероприятия' or message.text.lower() == 'events')
def events(message):
    if lang == 'ru':
        bot.send_message(message.chat.id, 'Будущие мероприятия: Летний лагер ШАГ')
    else:
        bot.send_message(message.chat.id, 'Future events: Summer ISTEP camp')


# ----------------------------------------------------------Стоимость обучения----------------------------------------------------------
@bot.message_handler(func=lambda message: message.text.lower() == 'стоимость обучения' or message.text.lower() == 'cost training')
def cost_training(message):
    if lang == 'ru':
        bot.send_message(message.chat.id, 'Стоимость: 15 000 рублей')
    else:
        bot.send_message(message.chat.id, 'Cost: 200 dollars')


# ----------------------------------------------------------Конец обучения----------------------------------------------------------
@bot.message_handler(func=lambda message: message.text.lower() == 'конец обучения' or message.text.lower() == 'the end of the training')
def end_training(message):
    if lang == 'ru':
        bot.send_message(message.chat.id, 'Обучение закончится: 31 Мая')
    else:
        bot.send_message(message.chat.id, 'Training will end: 31 May')


# ----------------------------------------------------------Отзывы преподавателей----------------------------------------------------------
@bot.message_handler(func=lambda message: message.text.lower() == 'отзывы преподавателей' or message.text.lower() == 'teachers feedback')
def teachers_feedback(message):
    if lang == 'ru':
        bot.send_message(message.chat.id, 'Леонид: Способный малый, вообще клёвый парень')
    else:
        bot.send_message(message.chat.id, 'Jhon: Good boy, very cool on pairs')


bot.polling()
