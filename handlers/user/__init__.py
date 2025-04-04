from .start import start_router
from .echo import echo_router
from aiogram import Router

user_router = Router()
user_router.include_routers(start_router, echo_router)