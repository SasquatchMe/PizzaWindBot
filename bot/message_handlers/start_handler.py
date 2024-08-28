from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.keyboards.quiz_inline_keyboard import quiz_inline_keyboard

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        text='Привет! Рад тебя видеть!',
        reply_markup=quiz_inline_keyboard(),
    )
