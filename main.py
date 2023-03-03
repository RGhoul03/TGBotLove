import telebot
import config
import test as t
import random
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def get_message(message):
    if message.text == '/start':
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton('Посчитать процент любви', callback_data='calc')
        markup.add(item1)
        bot.send_message(message.from_user.id, 'Приветик солнышко❤'
        '\nНапиши мне свое имя и имя твоего партнера, а я скажу процент любви между вами', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Я не понимаю тебя зайка')

@bot.message_handler(content_types=['text'])
def calc_love1(message):
    if '❤' in message.text:
        mes_txt = t.names(str(message.text))
        bot.send_message(message.chat.id, mes_txt)
    else:
        bot.send_message(message.chat.id, 'Уверен, что ты написал(а) что-то хорошее, но я не понимаю😔❤')

@bot.callback_query_handler(func=lambda call: True)
def calc_love2(call):
    if call.message:
        if call.data == 'calc':
            bot.send_message(call.message.chat.id, 'Напиши свое имя и имя партнера в формате: "(имя) и (имя)❤"'
                                                   '\nСердечко обязательно!')


bot.polling(none_stop=True, interval=0)