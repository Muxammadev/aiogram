from aiogram.filters import CommandStart
from aiogram.types import Message
from keyboards import reply
from aiogram import Router

start_router = Router()

@start_router.message(CommandStart())
async def start_handler(message: Message):
    user = message.from_user
    await message.reply(
        text=f"Salom <b>{user.first_name}</b> 👋 Template Botga hush kelibsiz! \n\n©️ <i>Ushbu bot @MuxammadDev tomonidan yaratilgan.</i>",
        reply_markup=reply.main_menu
    )
