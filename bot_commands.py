from telegram import Update
from telegram.ext import Updater, CommandHandler, ContextTypes, CallbackContext
import datetime
from spy import *
import pyowm
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

def hi_command(update: Update, context: CallbackContext): 
    log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}')

def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'/hi\n/time\n/help\n/sum\n/weather')   

def time_command(update: Update, context: CallbackContext): 
    log(update, context)
    update.message.reply_text(f'{datetime.datetime.now().time()}')

def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() #/sum 123 534543
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x+y}')   

def weather_command(update: Update, context: CallbackContext):
    log(update, context)
    config_dict = get_default_config()
    config_dict['language'] = 'ru'
    owm = OWM('82547a1146b5f5312210b1dfae35807e', config_dict)

    place = 'Лондон'  
    msg = update.message.text
    items = msg.split()
    place = items[1]
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    weather = observation.weather

    temp = weather.temperature('celsius')['temp']
    status = weather.detailed_status

    update.message.reply_text(f'В городе {place} сейчас {status}\n Температура в городе {temp}')   