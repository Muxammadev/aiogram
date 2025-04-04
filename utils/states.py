from aiogram.fsm.state import StatesGroup, State

# Bu yerda kerakli statelar yaratiladi.
class ExampleState(StatesGroup):
    first_state = State()
    second_state = State()
    third_state = State()
