from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# набор кнопок под сценарий
def get_main_keyboard():
  """Main bot keyboard"""
  keyboard = [
    [KeyboardButton(text="Анализировать текст")],
    [KeyboardButton(text="Помощь")]
  ]
  return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def get_analyze_keyboard():
  """Analyze page keyboard"""
  keyboard = [
    [KeyboardButton(text = "Выйти в главное меню")]
  ]
  keyboard = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
  return keyboard