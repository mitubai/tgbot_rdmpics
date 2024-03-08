from aiogram import types, Router
import logging

myinfo_router = Router()


@myinfo_router.message("myinfo")
async def myinfo(message: types.Message):
    logging.info(message.from_user)
    await message.answer(
        f"Ваш Id:, {message.from_user.id},"
        f"\n" f"Ваше Имя:, {message.from_user.first_name},"
        f"\n" f"Ваш никнейм: {message.from_user.username}\n")
