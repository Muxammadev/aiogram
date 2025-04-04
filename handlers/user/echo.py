from aiogram.types import Message
from keyboards import reply
from aiogram import Router

echo_router = Router()

@echo_router.message()
async def echo_handler(message: Message):
    user = message.from_user
    await message.copy_to(chat_id=user.id, reply_markup=reply.remove_menu)
