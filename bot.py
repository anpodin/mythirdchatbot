# -*- coding: utf-8 -*-
import telebot

bot = telebot.TeleBot("607967748:AAGGCS5t8TK7aKxZUeav2sgwcPTmkpVJDls")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
bot.reply_to(message, message.text)

bot.polling()
