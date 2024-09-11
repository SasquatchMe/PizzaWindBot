import random
import string

import requests
from pydantic import BaseModel


class SPromocode(BaseModel):
    code: str
    corrects: int
    is_active: bool


def generate_promocode(correct_answers: int) -> str:
    # Набор символов: заглавные буквы и цифры
    chars = string.ascii_uppercase + string.digits

    # Генерация 4-значного промокода
    promocode = "".join(random.choice(chars) for _ in range(4))

    promocode_dto = SPromocode(code=promocode, corrects=correct_answers, is_active=True)

    response = requests.post(
        url="http://main-app:8000/promocodes",
        json=promocode_dto.model_dump(),  # Используем params для query-параметров
    )

    # Проверка успешности запроса
    if response.status_code == 200:
        print("Промокод успешно отправлен.")
    else:
        print(f"Ошибка отправки промокода: {response.status_code} - {response.text}")

    return promocode
