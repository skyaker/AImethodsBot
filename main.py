import asyncio
from src.bot.handlers import register_handlers
from src.bot.bot import bot, dp

async def main():
  register_handlers(dp)
  
  try:
    print("Бот запущен...")
    await dp.start_polling(bot)
  finally:
    await bot.session.close()

if __name__ == "__main__":
  asyncio.run(main())
