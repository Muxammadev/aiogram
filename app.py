from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode
from data import BOT_TOKEN, ADMIN
from handlers import main_router
import asyncio

defaults = DefaultBotProperties(parse_mode=ParseMode.HTML)
storage = MemoryStorage()

bot = Bot(token=BOT_TOKEN, default=defaults)
dp = Dispatcher(storage=storage)

async def startup(tg: Bot):
    await tg.send_message(chat_id=ADMIN, text="Bot ishga tushdi.")

async def shutdown(tg: Bot):
    await tg.send_message(chat_id=ADMIN, text="Bot to'xtatildi.")
    await tg.delete_webhook()

async def main():
    dp.include_router(main_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())