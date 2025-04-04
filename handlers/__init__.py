from .channel import channel_router
from .admin import admin_router
from .group import group_router
from .user import user_router
from aiogram import Router

main_router = Router()

main_router.include_routers(user_router, admin_router, group_router, channel_router)

