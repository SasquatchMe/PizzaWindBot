from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def inline_deactive_promo(code_id: int):

    button = [
        InlineKeyboardButton(
            text="Погасить код",
            callback_data=f"deactive_promo:{code_id}",
        )
    ]

    markup = InlineKeyboardMarkup(
        inline_keyboard=[button],
    )

    return markup
