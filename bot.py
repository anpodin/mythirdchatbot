# -*- coding: utf-8 -*-
import telebot

bot = telebot.TeleBot("607967748:AAGGCS5t8TK7aKxZUeav2sgwcPTmkpVJDls")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот Андрея, давай поговорим? 🤖")

@bot.message_handler(commands=['ping'])  # This is just to check if the bot is online. Nothing special
def pong(m):
    bot.reply_to(m, 'Pong!')
    
@bot.message_handler(commands=['Привет'])  # Отвечаем на Привет
def hello(m):
    cid = m.chat.id
    bot.send_message(cid, 'Привет! Рад поговорить с тобой! 😋')
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
   cid = message.chat.id
   bot.send_message(cid, "Ой все! Хватит болтать 😆")

bot.polling(none_stop=True)
