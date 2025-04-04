from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardRemove

class ReplyKeyboard:
    def __init__(self):
        self.builder = ReplyKeyboardBuilder
        self.button = KeyboardButton
        self.remover = ReplyKeyboardRemove

    @property
    def remove_menu(self):
        return self.remover()

    @property
    def main_menu(self):
        return self.builder(
            markup=[
                [
                    self.button(text="1-TUGMA")
                ],
                [
                    self.button(text="2-TUGMA"),
                    self.button(text="3-TUGMA")
                ]
            ]
        ).as_markup(resize_keyboard=True)
