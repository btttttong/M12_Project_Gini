from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv
import os


load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

async def start(update: Update, context):
    welcome_message = "Sawadee Harbour Space students! Welcome to GiniBot, your pocket guide to awesome places and essentials in Bangkok, Thailand. Please select a place to go below, and I'll recommend some great options for you."
    markup = ReplyKeyboardMarkup([['Cafe', 'Restaurant', 'Hospital']])
    await update.message.reply_text(welcome_message, reply_markup=markup)

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler(command='start', callback=start))
    app.run_polling()

if __name__ == '__main__':
    main()