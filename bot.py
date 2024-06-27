from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
WEB_APP_URL = 'http://127.0.0.1:5000'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Welcome! Check out this car image: {WEB_APP_URL}')

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
