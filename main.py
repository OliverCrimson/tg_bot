import os
from aiogram import Bot, Dispatcher, F
from app.handlers import router
import asyncio

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')


async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
