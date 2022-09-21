import telebot
import fetch_floor as fetch_floor
import os

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(token = API_KEY)

@bot.message_handler(commands=['sup', 'hello'])
def sup(message):
    bot.reply_to(message, "sup bro")

@bot.message_handler(commands=['getfloor', 'floor', 'get_floor'])
def get_floor(message):
    bot.send_message(message.chat.id, 'just a second (:')
    floors = fetch_floor.start()
    response = ""
    for key in floors:
        response += f"{key} floor is: {floors[key]}₳\n"
    bot.reply_to(message, response)

bot.polling()