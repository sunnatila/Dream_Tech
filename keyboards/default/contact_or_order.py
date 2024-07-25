from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton


contacts_or_orders = ReplyKeyboardBuilder(
    [
        [
            KeyboardButton(text='Kontaktlarni korish'),
            KeyboardButton(text='Buyurtmalarni korish'),
        ]
    ]
).adjust(2).as_markup(resize_keyboard=True)
