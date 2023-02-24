from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
import os

TOKEN=os.environ.get('TOKEN')
i=0
j=0

updater = Updater(TOKEN)
dp = updater.dispatcher

def start(update: Update, context:CallbackContext):
    bot = context.bot

    chat_id = update.message.chat.id

    btn1 = KeyboardButton(text=f"👍{i}")
    btn2 = KeyboardButton(text=f"👎{j}")

    keyboard = ReplyKeyboardMarkup([[btn1, btn2]], resize_keyboard=True)


    bot.sendMessage(chat_id, "LIKE and DISLIKE", reply_markup=keyboard)

def like_and_dislike(update: Update, context: CallbackContext):
    text = update.message.text
    bot = context.bot
    chat_id = update.message.chat.id
    global i
    global j
    if text[0]=='👍':
        i+=1

    if text[0]=='👎':
        j+=1

    btn1 = KeyboardButton(text=f"👍{i}")
    btn2 = KeyboardButton(text=f"👎{j}")

    keyboard = ReplyKeyboardMarkup([[btn1, btn2]], resize_keyboard=True)

    bot.sendMessage(chat_id, "salom" , reply_markup=keyboard)

        


dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.text, like_and_dislike))

updater.start_polling()
updater.idle()