from aiogram.fsm.state import State, StatesGroup


class Quest(StatesGroup):
    location = State()
    get_question = State()
    get_answer = State()
