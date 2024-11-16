from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_keyboard():
  """Main bot keyboard"""
  keyboard = [
    [KeyboardButton(text="Анализировать текст")],
    [KeyboardButton(text="Помощь")]
  ]
  return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
