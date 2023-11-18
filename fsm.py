from aiogram.fsm.state import StatesGroup, State


class States(StatesGroup):
    expanse_name = State()
    expanse_cost = State()


class ShowStates(StatesGroup):
    show_ex = State()
    count_days = State()
    show_ex_cost = State()
