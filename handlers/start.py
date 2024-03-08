from aiogram import types, Dispatcher, Router
from aiogram.filters import Command
import logging

start_router = Router()


@start_router.message(Command("start"))
async def start(message: types.Message):
    logging.info(message.from_user)
    await message.answer(f"Привет, {message.from_user.first_name}")
