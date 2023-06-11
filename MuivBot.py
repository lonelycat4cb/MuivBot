import telebot
import pyqrcode
from telebot import types
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

bot = telebot.TeleBot('5838447318:AAGlaNIsRiM2jHWU8XDNjepn45ZY-3mqQso')

# ----------------------------------------------------------Кнопки_языка_при_старте----------------------------------------------------------
btnLanguage = telebot.types.ReplyKeyboardMarkup()
btnLanguage.row('Русский🇷🇺')
btnLanguage.row('English🇬🇧')

# --------------------------------------QR_CODE----------------------------------QR_CODE-------------------------------------------

#big_code = pyqrcode.create("https://pypi.org/project/pyTelegramBotAPI/")
#big_code.png('codqrine12.png', scale=8, module_color=[0, 0, 0], background=[0xff, 0xff, 0xff])


# ----------------------------------------------------------Старт----------------------------------------------------------
@bot.message_handler(commands=['start', 'старт'])
def start_message(message):
    bot.send_message(message.chat.id, 'Выберите язык / Select language', reply_markup=btnLanguage)


# ----------------------------------------------------------Возврат_в_начало----------------------------------------------------------
@bot.message_handler(func=lambda
        message: message.text.lower() == '<Возврат в начало>'.lower() or message.text.lower() == '<Return to start>'.lower())
def btn_login_ru(message):
    start_message(message)


# ----------------------------------------------------------Возврат_назад----------------------------------------------------------
@bot.message_handler(
    func=lambda message: message.text.lower() == '<назад>'.lower() or message.text.lower() == '<back>'.lower())
def btn_back(message):
    btn_welcome(message)


# ----------------------------------------------------------Справочник_языка----------------------------------------------------------
dictMsg = {
    'en': {
        'Забыл логин': 'Forget login',
        'Забыл пароль': 'Forget password',
        '✒Введите пароль': '✒Enter password',
        'Welcome': 'Welcome',
        '<Возврат в начало>': '<Return to start>',
        'Средний балл': 'Average score',
        'Посещаемость': 'Attendance',
        'Мероприятия': 'Events',
        'Стоимость ₽': 'Cost $',
        'Конец обучения': 'The end of the training',
        'Отзывы': 'Feedback',
        'Когда пара?': 'When pairs?',
        'Где пара?': 'Where pairs?',
        '<Назад>': '<Back>',
        'Оплата': 'Payment',
        'Контакты': 'Contacts',
        'Расписание': 'Schedule',
        'Рейтинг': 'Rating',
        'Повторите Авторизацию': 'Repeat Authorize'
    },
    'ru': {
        'Забыл логин': 'Забыл логин',
        'Забыл пароль': 'Забыл пароль',
        '✒Введите пароль': '✒Введите пароль',
        'Welcome': 'Добро пожаловать!',
        '<Возврат в начало>': '<Возврат в начало>',
        'Средний балл': 'Средний балл',
        'Посещаемость': 'Посещаемость',
        'Мероприятия': 'Мероприятия',
        'Стоимость ₽': 'Стоимость ₽',
        'Конец обучения': 'Конец обучения',
        'Отзывы': 'Отзывы',
        'Когда пара?': 'Когда пара?',
        'Где пара?': 'Где пара?',
        '<Назад>': '<Назад>',
        'Оплата': 'Оплата',
        'Контакты': 'Контакты',
        'Расписание': 'Расписание',
        'Рейтинг': 'Рейтинг',
        'Повторите Авторизацию': 'Повторите Авторизацию'
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

# ----------------------------------------------------------Авторизация_на_русском-------------------------------------------------------------
@bot.message_handler(func=lambda message: message.text.lower() == 'русский🇷🇺')
def btn_login_ru(message):
    global awaitAuth, lang
    awaitAuth = 1
    lang = 'ru'
    k = telebot.types.ReplyKeyboardMarkup()
    k.row('Забыл логин')
    k.row('<Возврат в начало>')
    bot.send_message(message.chat.id, '✏Введите ваш логин:', reply_markup=k)


# ----------------------------------------------------------Авторизация_на_английском----------------------------------------------------------
@bot.message_handler(func=lambda message: message.text.lower() == 'english🇬🇧')
def btn_login_en(message):
    global awaitAuth, lang
    awaitAuth = 1
    lang = 'en'
    k = telebot.types.ReplyKeyboardMarkup()
    k.row('Forget login')
    k.row('<Return to start>')
    bot.send_message(message.chat.id, '✏Enter login:', reply_markup=k)


# ----------------------------------------------------------Сохранение_логина------------------------------------------------------------------
@bot.message_handler(func=lambda message: message.content_type == 'text' and awaitAuth == 1)
def save_user_login(message):
    global uLogin, lang, awaitAuth
    awaitAuth = 2
    uLogin = message.text
    k = telebot.types.ReplyKeyboardMarkup()
    k.row('Забыл пароль')
    k.row('<Возврат в начало>')
    bot.send_message(message.chat.id, dictMsg[lang]['✒Введите пароль'])


# ----------------------------------------------------------Сохранение_пароля----------------------------------------------------------
@bot.message_handler(func=lambda message: message.content_type == 'text' and awaitAuth == 2)
def save_user_passwd(message):
    global uLogin, uPsswd, lang, awaitAuth
    browser = webdriver.Edge()
    browser.get("https://e.muiv.ru/login/index.php")
    elem_usr = browser.find_element(By.ID, 'username')
    elem_pas = browser.find_element(By.ID, 'password')
    elem_lgnbtn = browser.find_element(By.ID, 'loginbtn')

    awaitAuth = 0
    uPsswd = message.text

    for i in uLogin:
        elem_usr.send_keys(i)
        time.sleep(0.3)

    for n in uPsswd:
        elem_pas.send_keys(n)
        time.sleep(0.3)

    elem_lgnbtn.click()

    WebDriverWait(driver=browser, timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )
    error_message = "Неверный логин или пароль, попробуйте заново."
    errors = browser.find_elements(By.XPATH, '/html/body/div[2]/div[2]/div/div/section/div/div[2]/div/div/div/div/div[1]/div')
    if any(error_message in e.text for e in errors):
        print("[!] Login failed")
        btn_login_ru(message)
    else:
        print("[+] Login successful")
        btn_welcome(message)


# ----------------------------------------------------------Панель----------------------------------------------------------

def btn_welcome(message):
    k = telebot.types.ReplyKeyboardMarkup()
    bot.send_message(message.chat.id, dictMsg[lang]['Welcome'], reply_markup=k)
    k.row(dictMsg[lang]['Средний балл'], dictMsg[lang]['Посещаемость'], dictMsg[lang]['Стоимость ₽'],
          dictMsg[lang]['Оплата'])
    k.row(dictMsg[lang]['Конец обучения'], dictMsg[lang]['Отзывы'], dictMsg[lang]['Мероприятия'])
    k.row(dictMsg[lang]['Контакты'], dictMsg[lang]['Расписание'])
    k.row(dictMsg[lang]['Рейтинг'])
    k.row(dictMsg[lang]['<Возврат в начало>'])
    if lang == 'ru':
        bot.send_message(message.chat.id, 'Что вы хотите узнать?', reply_markup=k)
    else:
        bot.send_message(message.chat.id, 'What do you want to know?', reply_markup=k)


# ----------------------------------------------------------Рейтинг------------------------------------------------------------

@bot.message_handler(func=lambda message: message.text.lower() == 'рейтинг' or message.text.lower() == 'rating')
def rating(message):
    if lang == 'ru':
        bot.send_message(message.chat.id, 'Рейтинг:')
        bot.send_message(message.chat.id, 'Коля - 1003☆')
        bot.send_message(message.chat.id, 'Маша - 996☆')
        bot.send_message(message.chat.id, 'Арсений - 879☆')
        bot.send_message(message.chat.id, 'Алексей - 740☆')
    else:
        bot.send_message(message.chat.id, 'Rating:')
        bot.send_message(message.chat.id, 'Jhon - 1003☆')
        bot.send_message(message.chat.id, 'Anna - 996☆')
        bot.send_message(message.chat.id, 'Kate - 879☆')
        bot.send_message(message.chat.id, 'Stefania - 740☆')


# ----------------------------------------------------------Оплата------------------------------------------------------------

@bot.message_handler(func=lambda message: message.text.lower() == 'оплата' or message.text.lower() == 'payment')
def payment(message):
    if lang == 'ru':
        bot.send_message(message.chat.id, 'QR для оплаты:')
    else:
        bot.send_message(message.chat.id, 'QR for payment:')


# ----------------------------------------------------------Расписание----------------------------------------------------------
@bot.message_handler(
    func=lambda message: message.text.lower() == 'расписание' or message.text.lower() == 'schedule')
def schedule(message):
    if lang == 'ru':
        bot.send_message(message.chat.id, 'Уроки будут: 24 Мая, 31 Мая')
    else:
        bot.send_message(message.chat.id, 'Lessons will be: 24 May, 31 May')


# ----------------------------------------------------------Средний_балл----------------------------------------------------------

@bot.message_handler(
    func=lambda message: message.text.lower() == 'средний балл' or message.text.lower() == 'average score')
def average_score(message):
    if lang == 'ru':
        bot.send_message(message.chat.id, 'Ваш средний балл: 11')
    else:
        bot.send_message(message.chat.id, 'Your average score: 11')


# ----------------------------------------------------------Посещаемость----------------------------------------------------------
@bot.message_handler(
    func=lambda message: message.text.lower() == 'посещаемость' or message.text.lower() == 'attendance')
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


# ----------------------------------------------------------Стоимость_обучения----------------------------------------------------------

@bot.message_handler(
    func=lambda message: message.text.lower() == 'стоимость ₽' or message.text.lower() == 'cost $')
def cost(message):
    if lang == 'ru':
        bot.send_message(message.chat.id, 'Стоимость: 15 000 рублей')
    else:
        bot.send_message(message.chat.id, 'Cost: 200 dollars')


# ----------------------------------------------------------Конец_обучения----------------------------------------------------------

@bot.message_handler(
    func=lambda message: message.text.lower() == 'конец обучения' or message.text.lower() == 'the end of the training')
def end_training(message):
    if lang == 'ru':
        bot.send_message(message.chat.id, 'Обучение закончится: 31 Мая')
    else:
        bot.send_message(message.chat.id, 'Training will end: 31 May')


# ----------------------------------------------------------Отзывы_преподавателей----------------------------------------------------------

@bot.message_handler(
    func=lambda message: message.text.lower() == 'отзывы' or message.text.lower() == 'feedback')
def teachers_feedback(message):
    if lang == 'ru':
        bot.send_message(message.chat.id, 'Леонид: Способный малый, вообще клёвый парень')
    else:
        bot.send_message(message.chat.id, 'Jhon: Good boy, very cool on pairs')


# ----------------------------------------------------------Контакты----------------------------------------------------------

@bot.message_handler(
    func=lambda message: message.text.lower() == 'контакты' or message.text.lower() == 'contacts')
def contacts(message):
    if lang == 'ru':
        bot.send_message(message.chat.id, 'Приёмная: +74951511901')
        bot.send_message(message.chat.id, 'Учебная часть: +74951324400')
    else:
        bot.send_message(message.chat.id, 'Reception Office: +74951511901')
        bot.send_message(message.chat.id, 'Teaching Department: +74951324400')


bot.polling(none_stop=True)
