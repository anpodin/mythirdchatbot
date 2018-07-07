# -*- coding: utf-8 -*-
import telebot
token = '607967748:AAGGCS5t8TK7aKxZUeav2sgwcPTmkpVJDls'
bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет! Я третий бот Андрея. Спроси мена как дела.")
    
    elif message.text == "Как дела?" or message.text == "How are u?":
        bot.send_message(message.from_user.id, "Я в порядке! А вы?")
    
    else:
        bot.send_message(message.from_user.id, "Извини, я пока очень глуп. Не понимаю о чем ты. Давай начнем сначала.")
        
   bot.polling(none_stop=True, interval=0)
