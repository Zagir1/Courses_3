from aiogram import types
from utils import d_OG_api
from loader import dp

@dp.message_handler()
async def pw_generator(message: types.Message):
        await message.answer_photo(photo=d_OG_api.dog_pic())

