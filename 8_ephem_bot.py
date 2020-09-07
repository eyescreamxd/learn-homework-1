"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
from ephem import *
import logging
from setting import API_KEY
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)




PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}
def check_planet(bot, update):
    planet = str(update.message.text.split(' ')[1]).lower()
    if planet == 'mercury':
        update.message.reply_text(constellation(Mercury(now()))[-1])
    elif planet == 'venus':
        update.message.reply_text(constellation(Venus(now()))[-1])
    # elif planet == 'earth':
    #     update.message.reply_text(constellation(Earth(now()))[-1])
    elif planet == 'mars':
        update.message.reply_text(constellation(Mars(now()))[-1])
    elif planet == 'jupiter':
        update.message.reply_text(constellation(Jupiter(now()))[-1])
    elif planet == 'saturn':
        update.message.reply_text(constellation(Saturn(now()))[-1])
    elif planet == 'uranus':
        update.message.reply_text(constellation(Uranus(now()))[-1])
    elif planet == 'neptune':
        update.message.reply_text(constellation(Neptune(now()))[-1])


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
 

def main():
    mybot = Updater(API_KEY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", check_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
