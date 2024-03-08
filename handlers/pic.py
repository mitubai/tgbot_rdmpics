from aiogram import types, Dispatcher, Router
from aiogram.filters import Command
import logging
import random
from os import listdir, path

pic_router = Router()


@pic_router.message(Command("pic"))
async def pic(message: types.Message):
    image_directory = 'Images'
    file_name = random.choice(listdir(image_directory))
    file_path = path.join(image_directory, file_name)
    logging.info(file_path)
    file = types.InputFile(file_path)
    await message.answer_photo(file, caption="Котик")
    await message.reply("Котик")
