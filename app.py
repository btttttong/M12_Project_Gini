from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv
from utils import read_csv_with_column_filter
import random
import os


load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

async def start(update: Update, context):
    welcome_message = "Sawadee Harbour Space students! Welcome to GiniBot, your pocket guide to awesome places and essentials in Bangkok, Thailand. Please select a place to go below, and I'll recommend some great options for you."
    markup = ReplyKeyboardMarkup([['Cafe', 'Restaurant', 'Hospital']], one_time_keyboard=True)
    await update.message.reply_text(welcome_message, reply_markup=markup)


async def handle_reply(update, context):
    filename = 'data.csv'
    column_name = 'Category'
    option_selected = update.message.text.lower()

    csv_data = read_csv_with_column_filter(filename, column_name, option_selected)

    messages = [f"Below are the {option_selected}s I recommend:\n\n",
        f"Presenting my top {option_selected}s picks:\n\n",
        f"Here's a list of {option_selected}s I suggest:\n\n",
        f"I've curated a selection of {option_selected}s for you:\n\n",
        f"Check out my recommended {option_selected}s:\n\n"]

    await update.message.reply_text(random.choice(messages), parse_mode='HTML')
    for idx, row in enumerate(csv_data):
        if option_selected == 'hospital':
            text_with_link = f"<a href='{row[2]}'>\n<b>{idx+1}. {row[1]}</b></a>\n{row[4]}\nWith English support: {row[5]}\n\n"
        else:
            text_with_link = f"<a href='{row[2]}'>\n<b>{idx+1}. {row[1]}</b></a>\n{row[4]}\nPrice range: ฿{row[3]}\nWith English support: {row[5]}\nDelivery available: {row[6]}\n\n"
        message = text_with_link
        await update.message.reply_text(message, parse_mode='HTML')

   
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_reply))
    app.add_handler(CommandHandler(command='start', callback=start))
    
    app.run_polling()

if __name__ == '__main__':
    main()