from aiogram.filters.state import StatesGroup, State


class ContactState(StatesGroup):
    contact_user = State()
    contact_update = State()


class OrderState(StatesGroup):
    order_user = State()
    order_update = State()
