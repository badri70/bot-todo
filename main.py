import os
from aiogram import Bot, Dispatcher
import asyncio
from dotenv import load_dotenv
from router import router
from database import init_db

load_dotenv()
init_db()

bot = Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
dp = Dispatcher()


async def main():
    dp.include_router(router=router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

