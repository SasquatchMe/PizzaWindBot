from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery, ReplyKeyboardRemove

router = Router()

@router.callback_query(F.data == 'quiz')
async def quiz_callback(q: CallbackQuery):
    await q.message.edit_text(
        text='Нажмите /quest для начала игры!'
    )


