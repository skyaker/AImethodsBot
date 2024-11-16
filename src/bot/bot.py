import telebot
from dotenv import load_dotenv

load_dotenv()

token: str = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(token)