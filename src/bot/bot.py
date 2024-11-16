import os
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

load_dotenv()

token: str = os.getenv('BOT_TOKEN')

if not token:
  raise ValueError("Переменная окружения BOT_TOKEN не задана. Убедитесь, что .env файл в директории src/bot содержит BOT_TOKEN.")

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)