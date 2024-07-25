from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from loader import db


async def contacts_users():
    contact_ids = await db.get_contacts_ids()
    print(contact_ids)
    # contacts_status = db.get_contacts_status()
    contact_users = InlineKeyboardBuilder()
    for contact_id in contact_ids:
        contact_users.add(
            InlineKeyboardButton(text=f'{contact_id}-foydalanuvchi', callback_data=f"{contact_id}-foydalanuvchi"))
    return contact_users.adjust(3).as_markup()


async def contacts_status(user_id):
    statues = ['Kontakt yuborilgan', 'Rad etish', 'Xabar o\'qildi', 'Kelishilgan', 'Zakaz olingan', 'Javob berilgan']
    contact_user = await db.get_contact_from_id(user_id)
    contact_status = InlineKeyboardBuilder()
    for status in statues:
        contact_status.add(
            InlineKeyboardButton(text=f'{status}', callback_data=f"{status}-{contact_user[0]}"))
    return contact_status.adjust(2).as_markup()


async def orders_users():
    orders_ids = await db.get_orders_ids()
    order_users = InlineKeyboardBuilder()
    for order_id in orders_ids:
        order_users.add(
            InlineKeyboardButton(text=f'{order_id}-foydalanuvchi', callback_data=f"{order_id}-foydalanuvchi"))
    return order_users.adjust(3).as_markup()


async def orders_status(user_id):
    statues = ['Ariza yuborilgan', 'Rad etish', 'Qabul qilingan', 'Kelishilgan', 'Kelishilmagan',
               'Davom etayotgan proyekt', 'Tugatilgan proyekt']
    order_user = await db.get_order_from_id(user_id)
    order_status = InlineKeyboardBuilder()
    for status in statues:
        order_status.add(
            InlineKeyboardButton(text=f'{status}', callback_data=f"{status}-{order_user[0]}"))
    return order_status.adjust(2).as_markup()
