from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.quiz.keyboards.quiz_inline_keyboard import quiz_inline_keyboard
from bot.utils.greetings import get_greetings

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        text=get_greetings(),
        reply_markup=quiz_inline_keyboard(),
    )
