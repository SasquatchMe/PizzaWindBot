from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def quiz_inline_keyboard():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='🎮НАЧАТЬ КВЕСТ', callback_data='quiz'),
    )
    return builder.as_markup()

