from telegram import Update
from telegram.ext import Updater, CommandHandler, ContextTypes, CallbackContext
from bot_commands import *


updater = Updater("5483086087:AAGAKDUkx9Vw28DW39Z5f6hRIcgtwiI1YXM")

updater.dispatcher.add_handler(CommandHandler("hi", hi_command))
updater.dispatcher.add_handler(CommandHandler("time", time_command))
updater.dispatcher.add_handler(CommandHandler("help", help_command))
updater.dispatcher.add_handler(CommandHandler("sum", sum_command))
updater.dispatcher.add_handler(CommandHandler("weather", weather_command))

print('server start')


updater.start_polling()
updater.idle()









# import matplotlib.pyplot as plt
# import numpy as np

# list = [1, 2, 3, 2, 7]
# plt.plot(list)


# plt.show()








# import emoji

# print(emoji.emojize('Python is :thumbs_up:'))

# from progress.bar import Bar
# import time
 
# bar = Bar('Progressing', max = 20)
# for i in range (20):
#     time.sleep(1)
#     bar.next()
# bar.finish()


# from isOdd import isOdd

# print (isOdd(1))
# print (isOdd(4))