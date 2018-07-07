# -*- coding: utf-8 -*-
import telebot

bot = telebot.TeleBot("607967748:AAGGCS5t8TK7aKxZUeav2sgwcPTmkpVJDls")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот Андрея, давай поговорим?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    cid = message.chat.id
    if message.text = "Привет":
    bot.send_message(cid, "Привет! Поговори со мной!")
    elif:
    bot.send_message(cid, "Ой все! Хватит болтать :-D")

bot.polling(none_stop=True)
