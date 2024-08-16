from aiogram import Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start(message: Message) -> None:
    await message.answer(f'Привет, {message.from_user.full_name} я эхо-бот')


@dp.message()
async def echo(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer(f'Обвел меня')
