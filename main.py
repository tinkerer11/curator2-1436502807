from telebot import TeleBot

bot = TeleBot("7615100347:AAG9jksu_9Zmv1r1pYltLQWZ09H1XR0R0Ao")


@bot.message_handler(commands=['start'])
def few(message):
    bot.send_message(message.chat.id, 'Привет!')


@bot.message_handler(commands=['hello'])
def few(message):
    bot.send_message(message.chat.id, 'Я бот,созданный на марафоне Умскул!')


@bot.message_handler(commands=['Как_создать_бота?'])
def few(message):
    bot.send_message(message.chat.id, 'Переходи сюда! @BotFather')


@bot.message_handler(commands=['Где_можно_быстро_научиться_программированию?'])
def few(message):
    bot.send_message(message.chat.id, 'Переходи сюда! https://t.me/python2025_umschool')


@bot.message_handler(commands=['Где_можно_пройти_полноценный_курс_по_питону?'])
def few(message):
    bot.send_message(message.chat.id, 'Переходи сюда! https://pythonmarathon.tilda.ws/course')


bot.infinity_polling()