import random
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler

from telegram import ParseMode
import requests
import logging
import os 
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.getenv('TOKEN')
middle_finger = '\ud83d\udd95\ud83c\udfff'
hush = "\ud83e\udd2b"

def start(update,context):
    update.message.reply_text("yo")

def replymsg(update, context):
    name = update.message.from_user.first_name
    chat_id = update.message.chat.id
    random_num = random.randint(0, 7)
    message = update.message.text.lower().replace(" ","")
    if 'fuck' in message:
        update.message.reply_text("<b>KNN NO VULGARITIES U CB!!!!!</b> "+middle_finger, parse_mode = ParseMode.HTML)
    if 'who' in message:
        update.message.reply_text("Your mother", parse_mode = ParseMode.HTML)
    if random_num == 5:
        update.message.reply_text("Shut up la " + name + ' ' + hush, parse_mode = ParseMode.HTML)
    elif random_num == 6:
        url = 'https://cataas.com/cat'
        context.bot.send_photo(chat_id, url)
    elif random_num == 4:
        context.bot.send_message(chat_id, "Let's learn counting!")
        for number in range(20):
            context.bot.send_message(chat_id, number)
    
def main():
    updater = Updater(TOKEN)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    # Create command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, replymsg))

    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()

