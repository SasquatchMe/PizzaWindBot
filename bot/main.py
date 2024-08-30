import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.fsm.scene import SceneRegistry
from aiogram.fsm.storage.memory import SimpleEventIsolation

from bot.config import BOT_***
from bot.test import quiz_router, QuizScene
from bot.quiz.message_handlers.start_handler import router as start_router
from bot.quiz.callback_handlers.quiz_handler import router as start_quiz_router
from bot.quiz.message_handlers.quiz import router as quiz_router



async def main():
    bot = Bot(token=BOT_***)

    dp = Dispatcher(events_isolation=SimpleEventIsolation())

    dp.include_router(start_router)
    dp.include_router(start_quiz_router)
    dp.include_router(quiz_router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        stream=sys.stdout
                        )
    asyncio.run(main())
