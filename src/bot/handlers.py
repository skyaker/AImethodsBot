from aiogram import types, Router
from aiogram.filters import Command
from src.bot.bot import bot
from src.model.model import SentimentModel
from src.bot.keyboards import get_main_keyboard

router = Router()

sentiment_model = SentimentModel()

@router.message(Command(commands=["start"]))
async def start_command(message: types.Message):
    """Command handler /start"""
    keyboard = get_main_keyboard()
    await message.reply("Привет! Я бот для анализа тональности текста. Напишите любое сообщение, и я проанализирую его", reply_markup=keyboard)


@router.message(Command(commands=["help"]))
async def help_command(message: types.Message):
    """Command handler /help"""
    await message.reply("Необходимо отправить текстовое сообщение в чат, после чего я напишу результат анализа")


@router.message()
async def analyze_message(message: types.Message):
  """Message analyze handler"""
  try:
    result = sentiment_model.analyze_sentiment(message.text)
    label = result[0]["label"]
    score = result[0]["score"]
    await message.reply(f"Тональность: {label}\nУверенность: {score:.2f}")
  except Exception as e:
    await message.reply(f"Ошибка: {str(e)}")


@router.message(lambda message: message.text.lower() == "анализировать текст")
async def analyze_button(message: types.Message):
  """Button for analyzer"""
  await message.reply("Напишите текст, который хотите проанализировать")


@router.message(lambda message: message.text.lower() == "помощь")
async def help_button(message: types.Message):
  """Button for help"""
  await help_command(message)


def register_handlers(dp):
  dp.include_router(router)