from aiogram.fsm.state import State, StatesGroup


class Add_client(StatesGroup):
    age: State = State()
    full_name: State = State()
