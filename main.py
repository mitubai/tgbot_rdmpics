import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv
import logging

load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()


from handlers.start import start_router
from handlers.myinfo import myinfo_router
from handlers.pic import pic_router


async def main():
    dp.include_router(start_router)
    dp.include_router(myinfo_router)
    dp.include_router(pic_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
