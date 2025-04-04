from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


class InlineKeyboard:
    def __init__(self):
        self.builder = InlineKeyboardBuilder
        self.button = InlineKeyboardButton

    def main(self):
        return self.builder(
            markup=[
                [
                    self.button(text="1-TUGMA", callback_data="button_1"),
                ],
                [
                    self.button(text="2-TUGMA", callback_data="button_2"),
                    self.button(text="3-TUGMA", callback_data="button_3")
                ]
            ]
        ).as_markup(row_width=2)

