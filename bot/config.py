import os

from dotenv import load_dotenv

load_dotenv()


BOT_*** = os.getenv("BOT_***")

DEFAULT_COMMANDS = [
    {"command": "/start", "description": "Запустить бота"},
    {"command": "/help", "description": "Помощь"},
    {"command": "/quest", "description": "Начать квест!"},
]
