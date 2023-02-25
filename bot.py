from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
import os
import json

TOKEN=os.environ.get('TOKEN')

updater = Updater(TOKEN)
dp = updater.dispatcher

def start(update: Update, context:CallbackContext):
    bot = context.bot
    chat_id = update.message.chat.id


    try:
        with open('data.json','r') as f:
            data=json.loads(f.read())
        like = data[chat_id]['like']
        dislike = data[chat_id]['dislike']
    except:
        data={chat_id:{'like':0,'dislike':0}}
        with open('data.json','w') as f:
            json.dump(data,fp=f, indent=4)
        
    
    btn1 = KeyboardButton(text=f"👍{like}")
    btn2 = KeyboardButton(text=f"👎{dislike}")
    keyboard = ReplyKeyboardMarkup([[btn1, btn2]], resize_keyboard=True)
    bot.sendMessage(chat_id, 'Like and Dislike', reply_markup=keyboard)


def like_and_dislike(update: Update, context:CallbackContext):
    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id
    with open('data.json','r') as f:
        data=json.loads(f.read())
    like = data[chat_id]['like']
    dislike = data[chat_id]['dislike']        
    if text[0]=='👍':
        like+=1

    if text[0]=='👎':
        dislike+=1
    data[chat_id]['like'] = like
    data[chat_id]['dislike'] = dislike
    with open('data.json','w') as f:
        json.dump(data,fp=f, indent=4)

    btn1 = KeyboardButton(text=f"👍{like}")
    btn2 = KeyboardButton(text=f"👎{dislike}")

    keyboard = ReplyKeyboardMarkup([[btn1, btn2]], resize_keyboard=True)
    bot.sendMessage(chat_id,text,reply_markup=keyboard)
    
updater=Updater(TOKEN)
dp = updater.dispatcher
dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.text, like_and_dislike))

updater.start_polling()
updater.idle()