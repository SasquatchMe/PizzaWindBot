from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def location_inline_keyboard():

    button = [KeyboardButton(text='🧭Я НА МЕСТЕ', request_location=True)]
    keyboard = ReplyKeyboardMarkup(
        keyboard=[button],
        resize_keyboard=True,
        one_time_keyboard=True,
)
    return keyboard