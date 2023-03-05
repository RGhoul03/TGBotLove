import telebot
import config
import test as t
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

def start_markup():
    markup = types.InlineKeyboardMarkup(row_width=True)
    link = types.InlineKeyboardButton('Наш канал', url='https://t.me/Sborkapk2')
    check = types.InlineKeyboardButton('Проверить подписку', callback_data='check')
    markup.add(link, check)
    return markup

def love_markup():
    markup = types.InlineKeyboardMarkup(row_width=True)
    calc = types.InlineKeyboardButton('Посчитать процент любви', callback_data='calc')
    markup.add(calc)
    return markup

@bot.message_handler(commands=['start'])
def start_message(message):
    chat_id = message.chat.id
    first_name = message.chat.first_name
    bot.send_message(chat_id, f"Приветик {first_name}❤\n"
                              'Напиши мне свое имя и имя твоего партнера, а я скажу процент любви между вами\n'
                              "Но для начала нужно подписаться на канал", reply_markup=start_markup())

def check(call):
    status = ['creator', 'administrator', 'member']
    for i in status:
        if i == bot.get_chat_member(chat_id="-1001458108432", user_id=call.message.chat.id).status:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Спасибочки",reply_markup=love_markup())
            break
        else:
            bot.send_message(call.message.chat.id, "Котик, подпишись на канал", reply_markup=start_markup())

@bot.message_handler(content_types=['text'])
def calc_love1(message):
    if '❤' in message.text:
        mes_txt = t.names(str(message.text))
        bot.send_message(message.chat.id, mes_txt)
    else:
        bot.send_message(message.chat.id, 'Уверен, что ты написал(а) что-то хорошее, но я не понимаю😔❤')

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'calc':
            bot.send_message(call.message.chat.id, 'Напиши свое имя и имя партнера в формате: "(имя) и (имя)❤"'
                                                   '\nСердечко обязательно!')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Спасибочки", reply_markup=None)
        elif call.data == 'check':
            check(call)


bot.polling(none_stop=True, interval=0)