import  peewee
from pathlib import Path
import os
import telebot

from Maintenance import XML_Reader as reader

bot = telebot.TeleBot("698296687:AAFQl6Po6wpxBFXH-qHcrlii9BQCxFDkUJk")

ROOT_DIR = os.path.abspath(os.curdir)
PathToFile = Path(ROOT_DIR)
data = reader.get(PathToFile / "Maintenance" / "QASource.xml")


for i in data:
    v
    print(i['question'])
    print(i['answer'])


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Привет! Выбери один из пунктов меню.' + message.from_user.id, reply_markup=Menu.markup)

#@bot.message_handler(func= lambda message: True, content_types=['text'])
#def main_menu(message):
#    if var.is_exist_chatid_chat_id(message.chat.id) == 0:
#        name = 'NoName' if message.from_user.first_name == None else message.from_user.first_name
#        surname = 'NoSoname' if message.from_user.last_name == None else message.from_user.last_name
#        var.add_chatid(message.chat.id, name + ' ' + surname)
#    bot.reply_to(message, 'Привет! Выбери один из пунктов меню.', reply_markup=Menu.markup)


bot.polling()