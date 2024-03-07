import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from os import getenv
import logging
from random import choice

load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()

@dp.message(Command("myinfo"))
async def start(message: types.Message):
    logging.info(message.from_user)
    await message.answer(
        f"Ваш Id:, {message.from_user.id},\n" f"Ваше Имя:, {message.from_user.first_name},\n" f"Ваш никнейм: {message.from_user.username}\n")

@dp.message(Command("start"))
async def start(message: types.Message):
    logging.info(message.from_user)
    await message.answer(f"Привет, {message.from_user.first_name}")


@dp.message(Command("pic"))
async def pic(message: types.Message):
    photos = 'Images/1.png, Images/2.jpg, Images/3.png, Images/4.jpg, Images/5.png, Images/6.jpg, Images/7.jpg, Images/8.jpg, Images/9.jpg, Images/10.png'
    photo_paths = photos.split(', ')
    chosen_photo_path = choice(photo_paths)
    chosen_photo = types.FSInputFile(chosen_photo_path)
    await message.answer_photo(chosen_photo)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())