from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from bot.quiz.message_handlers.quiz import start_quest

router = Router()


@router.callback_query(F.data == "quiz")
async def quiz_callback(q: CallbackQuery, state: FSMContext):
    await start_quest(q.message, state)
