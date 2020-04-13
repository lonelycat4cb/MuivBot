import telebot
import pyqrcode
from telebot import types

bot = telebot.TeleBot('947044314:AAEsRIqbGcz5NtLJcyPJkjjVN6XD0ukKT_0')

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Мне нужна помощь!', 'QR (test)')

keyboard2 = telebot.types.ReplyKeyboardMarkup()
keyboard2.row('Где и когда пара?')
keyboard2.row('Когда каникулы?')
keyboard2.row('<Назад>')

keyboard21 = telebot.types.ReplyKeyboardMarkup()
keyboard21.row('Средний балл?', 'Посещаемость?', 'Мероприятия?')
keyboard21.row('Стоимость обучения?', 'Когда конец обучения?','Отзывы преподователей?')
keyboard21.row('<Назад>')

keyboard3 = telebot.types.ReplyKeyboardMarkup()
keyboard3.row('1.Родитель')
keyboard3.row('2.Ученик')
keyboard3.row('<Возврат в начало>')

keyboard = telebot.types.InlineKeyboardMarkup()
key_telec = telebot.types.InlineKeyboardButton('летний лагерь', callback_data='meropr')
keyboard.add(key_telec)

pay = str(11999)
sredball = str(11)
poseham = str(80)
otziv = str('ведет себя хорошо')
otzivyh = str('Леонид')
klass = '6.2'
time = '12:00'

a = str('1 июня')  # Просто переменная, чтобы не ругался компилятор
b = str('31 августа')  # Просто переменная, чтобы не ругался компилятор

#-----------------------------------------------------------------------------------------------------------------------

wwwqr = "https://www.youtube.com/watch?v=c8bOFSmVSuQ"
url = pyqrcode.create(wwwqr)
url.svg("myqr.svg", scale = 8)

#-----------------------------------------------------------------------------------------------------------------------

@bot.message_handler(commands=['start','старт'])
def start_message(message):
    bot.send_message(message.chat.id, 'Готов к работе!', reply_markup=keyboard1)

@bot.message_handler(content_types=['text','Photo'])
def send_text(message):
    if message.text.lower() == 'мне нужна помощь!':
        bot.send_message(message.chat.id, 'Кем вы являетесь?', reply_markup=keyboard3)

    elif message.text.lower() == 'QR (test)':
        bot.send_message(message.chat.id, 'qr:')

    elif message.text.lower() == '2.ученик':
        bot.send_message(message.chat.id, 'Вопросы, которые вы можете задать:', reply_markup=keyboard2)

    elif message.text.lower() == '1.родитель':
        bot.send_message(message.chat.id, 'Вопросы, которые вы можете задать:', reply_markup=keyboard21)


    elif message.text.lower() == 'где и когда пара?':
        bot.send_message(message.chat.id, 'пара в классе: ' + klass + ' в ' + time)


    elif message.text.lower() == 'посещаемость?':
        bot.send_message(message.chat.id, 'посещаемость за месяц = ' + poseham + ' %')

    elif message.text.lower() == 'мероприятия?':
        bot.send_message(message.chat.id, 'Мероприятия: ', reply_markup=keyboard)

    elif message.text.lower() == 'средний балл?':
        bot.send_message(message.chat.id, 'Средний балл ученик = ' + sredball)

    elif message.text.lower() == 'отзывы преподователей?':
        bot.send_message(message.chat.id, 'преподователь: ' + otzivyh + ' отзыв: ' + otziv)

    elif message.text.lower() == '<назад>':
        bot.send_message(message.chat.id, '<==>', reply_markup=keyboard3)

    elif message.text.lower() == '<возврат в начало>':
        bot.send_message(message.chat.id, '<=', reply_markup=keyboard1)

    elif message.text.lower() == '<возврат в начало>':
        bot.send_message(message.chat.id, '<=', reply_markup=keyboard1)

    elif message.text.lower() == 'cтоимость занятий' or message.text.lower() == 'cтоимость занятий?' \
        or message.text.lower() == 'стоимость обучения?' or message.text.lower() == 'стоимость обучения':
        bot.send_message(message.chat.id, 'Стоимость обучения: ...')


    elif message.text.lower() == 'когда каникулы' or message.text.lower() == 'когда каникулы?' \
        or message.text.lower() == 'когда конец обучения?' or message.text.lower() == 'когда конец обучения':
        bot.send_message(message.chat.id, 'Каникулы будут с ' + a + ' по ' + b)

    else:
        bot.send_message(message.from_user.id, "Я вас не понимаю")


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)


bot.polling()