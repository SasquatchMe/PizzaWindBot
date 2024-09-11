import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import SimpleEventIsolation

from bot_service.handlers.message_handlers import router as message_router
from bot_service.handlers.callback_handlers import router as callback_router

from bot_service.config import SERVICE_BOT_***


async def main():
    bot = Bot(token=SERVICE_BOT_***)

    dp = Dispatcher(events_isolation=SimpleEventIsolation())

    dp.include_router(
        message_router,
    )

    dp.include_router(
        callback_router,
    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
        stream=sys.stdout,
    )
    asyncio.run(main())
