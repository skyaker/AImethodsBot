from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from src.bot.bot import bot
from src.model.model import SentimentModel
from src.bot.keyboards import *

router = Router()

sentiment_model = SentimentModel()

class TextAnalysisState(StatesGroup):
  analyzing = State()

async def is_not_button(message: types.Message) -> bool:
  return message.text.lower() not in ["Анализировать текст", "Помощь"]


@router.message(Command(commands=["start"]))
async def start_command(message: types.Message):
  """Command handler /start"""
  keyboard = get_main_keyboard()
  await message.reply("Привет! Я бот для анализа тональности текста. Чем могу помочь?", reply_markup=keyboard)


@router.message(Command(commands=["help"]))
async def help_command(message: types.Message):
  """Command handler /help"""
  await message.reply("Нажмите на кнопку \"Анализировать текст\" и введите текстовое сообщение в чат, после чего я напишу результат анализа.")


@router.message(F.text == "Анализировать текст")
async def enter_analysis_mode(message: types.Message, state: FSMContext):
  await message.reply("Теперь вы можете отправить текст для анализа.", reply_markup=get_analyze_keyboard())
  await state.set_state(TextAnalysisState.analyzing)


@router.message(F.text == "Помощь")
async def help_button(message: types.Message):
  """Button for help"""
  await help_command(message)


@router.message(F.text == "Выйти в главное меню")
async def exit_analysis_mode(message: types.Message, state: FSMContext):
  await message.reply("Вы вышли в главное меню.", reply_markup=get_main_keyboard())
  await state.clear()


@router.message(TextAnalysisState.analyzing)
async def analyze_text(message: types.Message, state: FSMContext):
  """Message analyze handler"""
  try:
    result = sentiment_model.analyze_sentiment(message.text)
    label = result[0]["label"]
    score = result[0]["score"]
    await message.reply(f"Тональность: {label}\nУверенность: {score:.2f}")
  except Exception as e:
    await message.reply(f"Ошибка: {str(e)}")


def register_handlers(dp):
  dp.include_router(router)