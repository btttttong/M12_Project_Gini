# GiniBot: HS Bangkok Telegram Bot
<b>GiniBot</b> is a Telegram Chatbot designed for Harbour Space students in the Bangkok campus. The bot offers suggestions for amazing destinations and essential spots to explore throughout Thailand. Additionally, the bot also serves as an academic guide, offering assistance and resources for students. 



## Features
- **Suggestions with Google Maps Integration:** Offers advice on top attractions and vital facilities such as hospitals, with convenient links to Google Maps for easy navigation.
- **Access to Academic Resources:** Provides links to comprehensive information and staff details.


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
1. Start the bot by sending /start.
2. Reply to the bot or click on the menu with the desired main theme: /life or /school.
3. The bot will respond with a list of categories under each main theme.
4. Click the category of interest to display the information and the relevant links.

## Dependencies
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot): Python interface for the Telegram Bot API.
- [python-dotenv](https://github.com/theskumar/python-dotenv): Library for managing environment variables in a .env file.

