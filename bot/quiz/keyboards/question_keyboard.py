from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def question_keyboard(question, step):
    markup = ReplyKeyboardBuilder()
    markup.add(*[KeyboardButton(text=answer.text) for answer in question.answers])
    markup.button(text="🚫 Выход")

    return markup.adjust(2).as_markup(resize_keyboard=True)
