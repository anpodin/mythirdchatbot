# -*- coding: utf-8 -*-
import telebot

bot = telebot.TeleBot("607967748:AAGGCS5t8TK7aKxZUeav2sgwcPTmkpVJDls")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
bot.reply_to(message, "Привет! Я бот Андрея, как твои дела?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):

    if message.text == "Привет":
        bot.reply_to(message, "Привет! Как твои дела?")
    
    elif message.text == "Как дела?" or message.text == "How are u?":
        bot.reply_to(message, "Отлично!")
    
    else:
        bot.reply_to(message, "Извини, я очень глуп, ничего не понимаю, кроме привет и как дела...")

bot.polling(none_stop=True, interval=0)
