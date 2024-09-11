import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import SimpleEventIsolation
from aiogram.types import BotCommand

from bot.config import BOT_***, DEFAULT_COMMANDS
from bot.quiz.callback_handlers.quiz_handler import router as start_quiz_router
from bot.quiz.constants import GREETING
from bot.quiz.message_handlers.quiz import router as quiz_router
from bot.quiz.message_handlers.commands import router as start_router


async def main():
    bot = Bot(token=BOT_***)
    await bot.set_my_commands(
        [
            BotCommand(command=opts["command"], description=opts["description"])
            for opts in DEFAULT_COMMANDS
        ]
    )
    await bot.set_my_description(
        # description="Квест-БОТ by DVOR\nИграйте, исследуйте, получайте призы!"
        description=GREETING
    )
    await bot.set_my_short_description(short_description="Квест-БОТ by DVOR")

    dp = Dispatcher(events_isolation=SimpleEventIsolation())

    dp.include_router(start_router)
    dp.include_router(start_quiz_router)
    dp.include_router(quiz_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
        stream=sys.stdout,
    )
    asyncio.run(main())
