from telegram import Update
from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv
import os
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

async def start(update: Update, context):
    await update.message.reply_text('Sawadee khrap')

def main():
    app = Application.builder().token(BOT_TOKEN ).build()
    app.add_handler(CommandHandler(command='start', callback=start))
    app.run_polling()

if __name__ == '__main__':
    main()