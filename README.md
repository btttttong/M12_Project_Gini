# Project Gini: HS BKK Telegram Bot
GiniBot, designed for Harbour Space students in Bangkok, Thailand, is a Telegram Chatbot offering suggestions for fantastic destinations and essential spots to explore throughout Bangkok, Thailand.


## Features
- **Recommendations:** Provides recommendations based on user input.
- **Google Maps Integration:** Includes links to Google Maps for easy navigation to recommended places.
- **Interactive:** Offers a user-friendly interface for selecting recommendations.

## Setup
1. **Clone the Repository:**
   ```
   git clone https://github.com/btttttong/M12_Project_Gini
   cd M12_Project_Gini
   ```

2. **Install Dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Set Up Telegram Bot:**
   - Create a new bot using the BotFather on Telegram.
   - Obtain the bot token.

4. **Set Bot Token:**
  - Create a `.env` file in the root directory of your project.
  - Inside the `.env` file, add a line with `BOT_TOKEN=YOUR_ACTUAL_BOT_TOKEN`, replacing `YOUR_ACTUAL_BOT_TOKEN` with your bot token obtained from BotFather.

5. **Prepare Data (Optional):**
   - If you want to customize the recommendations, create a CSV file with your own data.

6. **Run the Bot:**
   ```
   python app.py
   ```

## Usage
To trigger the welcome message and option menu, start the bot by sending the command /start.

1. Start the bot by sending /start.
2. Reply to the bot with your desired category.
3. The bot will respond with a list of recommendations from the specified category with the corresponding Google Map link.

## Dependencies
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot): Python interface for the Telegram Bot API.
- [python-dotenv](https://github.com/theskumar/python-dotenv): Library for managing environment variables in a .env file.

