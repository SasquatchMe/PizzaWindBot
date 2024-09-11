import requests
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot_service.keyboards.inline_deactive_promo import inline_deactive_promo

router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(text="Пришлите код выданный гостю")


@router.message(F.text.func(lambda text: len(text) == 4))
async def promocode_handler(message: Message):
    promocode_data = requests.get(
        f"http://main-app:8000/promocodes/{message.text}"
    ).json()
    # promocode_data := requests.get(f"http://127.0.0.1:8000/promocodes/{message.text}").json()
    if promocode_data is not None:
        if promocode_data["is_active"]:
            corrects = promocode_data["corrects"]
            await message.answer(
                f"Промокод активен. Выигрыш по промокоду: {corrects * 10}% скидка",
                reply_markup=inline_deactive_promo(promocode_data["id"]),
            )

        else:
            await message.answer(f"Промокод уже погашен")

    else:
        await message.answer(f"Промокода не существует")


@router.message(F.text.func(lambda text: len(text) != 4))
async def promocode_invalid_handler(message: Message):
    await message.answer(f"Промокода не существует")
