from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp


@dp.message_handler(CommandStart())
async def cmd_start(message: types.Message):
    # Command '/start' handler
    await message.answer(text='Данный бот предназначен для получения картинки рандомной собаки')
