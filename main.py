from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import requests
import re


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


updater = Updater('1016464732:AAEoGlGEZfu4bWDfreOf7_d9zIu14E8K_wA', use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()
