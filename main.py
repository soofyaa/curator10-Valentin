
import telebot
from telebot import types
bot = telebot.TeleBot('6228137971:AAGZ3DH93cuo6mSkQD5pum9yMZ4Y4g8LMyI')


@bot.message_handler(commands=['start'])
def star_message(message):
    bot.send_message(message.chat.id,'Добро пожаловать в бот погоды')


@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1=types.KeyboardButton("Москва")
    button2 = types.KeyboardButton("Санкт-Петербург")
    button3 = types.KeyboardButton("Тюмень")
    button4 = types.KeyboardButton("Создатель бота")
    markup.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id, 'Выберите город', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == 'Москва':
        bot.send_message(message.chat.id,"Кто его знает, мне тепло и хорошо")
    elif message.text == 'Санкт-Петербург':
        bot.send_message(message.chat.id, "Настоящий петербуржец различает до тысячи оттенков серого.")
    elif message.text == 'Тюмень':
        bot.send_message(message.chat.id, "Странная твоя осень лучше дай снега")
    elif message.text == 'Создатель бота':
        bot.send_message(message.chat.id, "Я этого человек не когда не видел, но если он создал меня то он бог")


bot.infinity_polling()