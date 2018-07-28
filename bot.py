# -*- coding: utf-8 -*-
import telebot

bot = telebot.TeleBot("607967748:AAGGCS5t8TK7aKxZUeav2sgwcPTmkpVJDls")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hi! I am Andrey's bot 🤖 Please send me a photo and I will tell what I see🔬")

@bot.message_handler(commands=['ping'])  # This is just to check if the bot is online. Nothing special
def pong(m):
    bot.reply_to(m, 'Pong!')
    
@bot.message_handler(commands=['привет'])  # Отвечаем на Привет
def hello(m):
    cid = m.chat.id
    bot.send_message(cid, 'Привет! Рад поговорить с тобой! 😋')
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
   cid = message.chat.id
   txt = message.text
   if txt == 'Привет':
        bot.send_message(cid, "Привет! Рад поговорить с тобой! 😋")
   elif txt == 'Как дела?':
        bot.send_message(cid, "Лучше всех! 👌")
   elif txt == 'Hi':
        bot.send_message(cid, "Hi! 😋 How are you?")
   else:
        bot.send_message(cid, "OK let's get down to business - pls send me a photo! 📸")

def processPhotoMessage(message):
    cid = message.chat.id
    fileID = message.photo[-1].file_id
    file = bot.get_file(fileID)
    path = file.file_path
    url = "https://api.telegram.org/file/bot607967748:AAGGCS5t8TK7aKxZUeav2sgwcPTmkpVJDls/" + path
    
    import requests
    r = requests.post(
    "https://api.deepai.org/api/demographic-recognition",
    data={
        'image': url,
    },
    headers={'api-key': '104f12a5-1dae-402d-b4b6-bb24b6b501b4'}
    )
    import json
    age =  r.json()['age_range'] 
    gender = r.json()['gender'] 
    race = r.json()['cultural_appearance']
    talk = "Age: " + age + ".  Gender: " + gender + ".  Race: " + race
    bot.send_message(cid, talk)


@bot.message_handler(content_types=['photo'])  # This one is to get an image and process it through DeepAI
def photo(message):
    processPhotoMessage(message)

    

bot.polling(none_stop=True)
