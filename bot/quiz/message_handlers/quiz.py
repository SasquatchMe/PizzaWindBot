import asyncio

from aiogram import Router, F, html
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.utils.formatting import (
    as_list,
    as_section,
    Bold,
    as_numbered_list,
    as_key_value,
)

from bot.quiz.constants import SHORT_FAQ
from bot.quiz.keyboards.location_inline_keyboard import location_inline_keyboard
from bot.quiz.keyboards.question_keyboard import question_keyboard
from bot.quiz.states.states import Quest
from bot.utils.generate_promocode import generate_promocode
from bot.utils.geopos import check_geopos
from bot.utils.get_questions import get_questions
from bot.utils.get_url import get_url

router = Router()


@router.message(Command("quest"))
async def start_quest(message: Message, state: FSMContext, step: int = 0):
    await state.set_state(Quest.location)
    await state.update_data(step=step)
    if step == 0:
        await state.update_data(questions=get_questions())
        await message.answer(text=SHORT_FAQ)
        await asyncio.sleep(10)

        await message.answer(
            text="Квест начинается!", reply_markup=ReplyKeyboardRemove()
        )
        await asyncio.sleep(1)

    data = await state.get_data()
    try:
        question = data["questions"][step]
    except IndexError:
        await message.answer(text="Завершение квеста...")
        await exit_quest(message, state)
    else:
        if step == 0:
            await message.answer(
                text="Первый вопрос!", reply_markup=ReplyKeyboardRemove()
            )
        else:
            await message.answer(
                text="Следующий вопрос!", reply_markup=ReplyKeyboardRemove()
            )

        await asyncio.sleep(1)
        await message.answer(
            text=f"Беги [СЮДА]({get_url(question.location[0], question.location[1])})",
            reply_markup=location_inline_keyboard(),
            parse_mode=ParseMode.MARKDOWN,
        )
        await asyncio.sleep(1)


@router.message(Quest.location, F.content_type == "location")
async def check_location(message: Message, state: FSMContext):
    lat = message.location.latitude
    lon = message.location.longitude
    data = await state.get_data()
    step = data["step"]
    question = data["questions"][step]
    r_lat = question.location[0]
    r_lon = question.location[1]

    dis = check_geopos((lat, lon), (r_lat, r_lon))

    if dis:
        await state.set_state(Quest.get_question)
        await send_question(message, state)
        await asyncio.sleep(1)
    else:
        await message.answer(
            text="Нужно подойти к точке, чтобы получить вопрос.\n"
            'Пожалуйста, подойди ближе и нажми еще раз кнопку "🧭Я НА МЕСТЕ"'
        )
        await asyncio.sleep(1)


@router.message(F.text == "🚫 Выход")
async def exit_quest(message: Message, state: FSMContext):
    data = await state.get_data()
    answers = data.get("answers", {})
    questions = data["questions"]

    correct = 0
    incorrect = 0
    user_answers = []
    for step, quiz in enumerate(questions):
        answer = answers.get(step)
        is_correct = answer == quiz.correct_answer
        if is_correct:
            correct += 1
            icon = "✅"
        else:
            incorrect += 1
            icon = "❌"
        if answer is None:
            answer = "no answer"
        user_answers.append(f"{quiz.text} ({icon} {html.quote(answer)})")

    content = as_list(
        as_section(
            Bold("Твои ответы"),
            as_numbered_list(*user_answers),
        ),
        "",
        as_section(
            Bold("Итого"),
            as_list(
                as_key_value("Правильных", correct),
                as_key_value("Неправильных", incorrect),
            ),
        ),
    )

    await message.answer(**content.as_kwargs(), reply_markup=ReplyKeyboardRemove())
    if correct > 0:
        promocode = generate_promocode(correct)

        await message.answer(
            text=f'Поздравляем, Вы выиграли {correct * 10}% скидку в "Пицца-портале"! '
            f"Ваш промокод: {promocode}. Покажите его нашему кассиру!"
        )
    else:
        await message.answer(
            text=f"В этот раз Вам не повезло :( Попробуйте еще раз, Вы точно справитесь лучше!"
        )

    await state.set_data({})
    await state.clear()


@router.message(Quest.get_question, F.text)
async def get_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    step = data["step"]
    answers = data.get("answers", {})
    answers[step] = message.text
    await state.update_data(answers=answers)
    new_data = await state.get_data()

    await message.answer(text=f"Ответ принят!")
    await asyncio.sleep(2)

    await start_quest(message, state, step=step + 1)


async def send_question(message: Message, state: FSMContext):
    data = await state.get_data()
    step = data["step"]
    question = data["questions"][step]

    await message.answer(
        text=question.text,
        reply_markup=question_keyboard(question=question, step=step),
    )
