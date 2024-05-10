from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv
from utils import read_csv_with_column_filter
import random
import os


load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')



async def start(update: Update, context):
    first_name = update.message.chat.first_name
    welcome_message = f"""<b style='font-size: 24px;'>🌟 Hey {first_name}! 🌟</b>\n\nI am <b>Gini</b>, your virtual assistant tailored for the lifestyle and academic needs of students at Harbour Space Bangkok.

<b>Commands 💬</b>
You can control me by clicking any option below or sending these commands.

🇹🇭  /life - explore must-visit places and essentials in Thailand
📚  /school - search school-related resources
🤖  /aboutme - describe the functionality of the bot
"""
    markup = ReplyKeyboardMarkup([['/life', '/school']], one_time_keyboard=True)
    await update.message.reply_text(welcome_message, parse_mode="HTML", reply_markup=markup)

async def aboutme(update: Update, context):
    description = """I am Telegram bot developed by Gino and BT under Anton Topchii's supervision.
    
My purpose is to act as your personal virtual assistant, offering suggestions for exciting places to visit and must-see attractions in Thailand. Furthermore, I'm here to support you academically, providing aid and resources for your studies.

If you have any feature requests, feel free to <a href="mailto:ginoasuncion@gmail.com">email us</a> at ginoasuncion@gmail.com or <a href="mailto:supakavadee.r@gmail.com">supakavadee.r@gmail.com</a>."""

    await update.message.reply_text(description, parse_mode="HTML")


async def life(update: Update, context):
    welcome_message = "Please select a place to go below, and I'll recommend some great options for you."
    markup = ReplyKeyboardMarkup([['Cafe', 'Restaurant', 'Hospital']], one_time_keyboard=True)
    await update.message.reply_text(welcome_message, reply_markup=markup)

async def school(update: Update, context):
    welcome_message = "Please select a category, and I'll provide you with relevant links."
    markup = ReplyKeyboardMarkup([['International Students', 'Staff']], one_time_keyboard=True)
    await update.message.reply_text(welcome_message, reply_markup=markup)

async def handle_reply(update, context):
    option_selected = update.message.text.lower()

    if option_selected in ['cafe', 'restaurant', 'hospital']:
        filename = 'data/life.csv'
        column_name = '\ufeffCategory'
        
        csv_data = read_csv_with_column_filter(filename, column_name, option_selected)

        messages = [f"<b>Below are the {option_selected}s I recommend:</b>\n\n",
            f"<b>Presenting my top {option_selected}s picks:</b>\n\n",
            f"<b>Here's a list of {option_selected}s I suggest:</b>\n\n",
            f"<b>I've curated a selection of {option_selected}s for you:</b>\n\n",
            f"<b>Check out my recommended {option_selected}s:</b>\n\n"]
        
        if option_selected == 'cafe':
            await update.message.reply_text('☕  ' + random.choice(messages), parse_mode='HTML')
        elif option_selected == 'restaurant':
            await update.message.reply_text('🍝  ' + random.choice(messages), parse_mode='HTML')
        elif option_selected == 'hospital':
            await update.message.reply_text('🏥  ' + random.choice(messages), parse_mode='HTML')

        for idx, row in enumerate(csv_data):
            if option_selected == 'hospital':
                text_with_link = f"<a href='{row[2]}'>\n<b>{idx+1}. {row[1]}</b></a>\n{row[4]}\nWith English support: {row[5]}\n\n"
            else:
                text_with_link = f"<a href='{row[2]}'>\n<b>{idx+1}. {row[1]}</b></a>\n{row[4]}\nPrice range: ฿{row[3]}\nWith English support: {row[5]}\nDelivery available: {row[6]}\n\n"
            message = text_with_link
            await update.message.reply_text(message, parse_mode='HTML')
    
    elif option_selected in ['staff', 'international students']:
        filename = 'data/school.csv'
        column_name = '\ufeffCategory'
        
        csv_data = read_csv_with_column_filter(filename, column_name, option_selected)

        messages = [f"Below are the {option_selected}s I recommend:\n\n",
        f"Presenting my top {option_selected}s picks:\n\n",
        f"Here's a list of {option_selected}s I suggest:\n\n",
        f"I've curated a selection of {option_selected}s for you:\n\n",
        f"Check out my recommended {option_selected}s:\n\n"]

        # await update.message.reply_text(random.choice(messages), parse_mode='HTML')
        for idx, row in enumerate(csv_data):
            if option_selected == 'international students':
                message = f"""‼️ <b>Important Reminders for International Students</b> ‼️

{row[4]}

For detailed information related to visa and immigration requirements for international students, please go to this <a href='{row[5]}'>link</a>."""
                await update.message.reply_text(message, parse_mode='HTML')

        if option_selected == 'staff':
            message = f"🏫 <b>Here are the amazing staff of Harbour Space:</b> 🏫\n"
            await update.message.reply_text(message, parse_mode='HTML')
            for idx, row in enumerate(csv_data):
                message = f"<a href='{row[5]}'><b>{row[1]}</b></a>\n{row[2]}\nEmail: <a href='{row[3]}'>{row[3]}</a>\n\n"
                await update.message.reply_text(message, parse_mode='HTML')

   
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_reply))
    app.add_handler(CommandHandler(command='start', callback=start))
    app.add_handler(CommandHandler(command='life', callback=life))
    app.add_handler(CommandHandler(command='school', callback=school))
    app.add_handler(CommandHandler(command='aboutme', callback=aboutme))
    app.run_polling()

if __name__ == '__main__':
    main()