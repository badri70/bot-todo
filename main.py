import os
from aiogram import Bot, Dispatcher
import asyncio
from dotenv import load_dotenv
from . import router


load_dotenv()

bot = Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
dp = Dispatcher()


async def main():
    dp.include_router(router=router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

