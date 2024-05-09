from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv
from utils import read_csv_with_column_filter
import os


load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

async def start(update: Update, context):
    welcome_message = "Sawadee Harbour Space students! Welcome to GiniBot, your pocket guide to awesome places and essentials in Bangkok, Thailand. Please select a place to go below, and I'll recommend some great options for you."
    markup = ReplyKeyboardMarkup([['Cafe', 'Restaurant', 'Hospital']], one_time_keyboard=True)
    await update.message.reply_text(welcome_message, reply_markup=markup)


async def handle_reply(update, context):
    filename = 'ginidata.csv'
    column_name = '\ufeffCategory'
    option_selected = update.message.text
    csv_data = read_csv_with_column_filter(filename, column_name, option_selected)
    message = "Here are my recommendations:\n\n"
    await update.message.reply_text(message, parse_mode='HTML')
    for idx, row in enumerate(csv_data):
        text_with_link = f"<a href='{row[2]}'>{idx+1}. {row[1]}</a>\n"
        message = text_with_link
        await update.message.reply_text(message, parse_mode='HTML')

   
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_reply))
    app.add_handler(CommandHandler(command='start', callback=start))
    
    app.run_polling()

if __name__ == '__main__':
    main()