from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardBuilder


# confirm_no_confirm = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton("Kelishilgan", callback_data='confirm'),
#             InlineKeyboardButton("Rad etish", callback_data='not_confirm'),
#
#         ],
#     ], row_width=2
# )


async def confirm_no_confirm(user_id):
    inline_buttons = InlineKeyboardBuilder(
        [
            [
                InlineKeyboardButton(text='Kelishilgan', callback_data=f"Kelishilgan_{user_id}"),
                InlineKeyboardButton(text='Rad etish', callback_data=f"Rad etish_{user_id}"),
            ]
        ]
    )
    return inline_buttons.adjust(2).as_markup()
