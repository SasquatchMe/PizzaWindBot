import requests
from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query()
async def deactive_promo(q: CallbackQuery):
    code_id = q.data.split(":")[1]
    response = requests.patch(
        # url=f"http://127.0.0.1:8000/promocodes/deactivate/{code_id}"
        url=f"http://main-app:8000/promocodes/deactivate/{code_id}"
    )
    # response = requests.patch(url=f'http://main-app/promocodes/deactivate/{code_id}')

    await q.message.edit_reply_markup(reply_markup=None)
    await q.message.edit_text("Промокод погашен, пробейте скидку гостю")
