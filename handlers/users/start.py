import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from aiogram import types, F
from aiogram.filters import CommandStart, Filter
from aiogram.types import CallbackQuery
from keyboards.inline.Confirm import confirm_no_confirm
from data.config import ADMINS
from loader import bot, db, dp
from keyboards.default import contacts_or_orders
import asyncio


class AdminFilter(Filter):
    async def __call__(self, msg: types.Message):
        return lambda obj: str(msg.from_user.id) in ADMINS


@dp.message(CommandStart(), AdminFilter())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=contacts_or_orders)


async def send_contact_info(user_id, fullname, phone, message):
    await asyncio.sleep(5)
    for admin in ADMINS:
        info = f"📞 Kontakt bilan bog'lanish:\n"
        info += f"👤 Foydalanuvchining id raqami:   {user_id}\n\n"
        info += f"👤 Foydalanuvchining ismi:   {fullname}\n\n"
        info += f"📱 Telefon raqam: <a href='tel: +998{phone}'>+998{phone}</a>\n\n"

        info += f"📝 Foydalanuvchining maqsadi:\n\n{message}"
        await bot.send_message(chat_id=admin, text=info, reply_markup=await confirm_no_confirm(user_id))
        await bot.session.close()


async def send_contact_info_full_number(user_id, fullname, phone, message):
    await asyncio.sleep(5)
    for admin in ADMINS:
        info = f"📞 Kontakt bilan bog'lanish:\n"
        info += f"👤 Foydalanuvchining id raqami:   {user_id}\n\n"
        info += f"👤 Foydalanuvchining ismi:   {fullname}\n\n"
        info += f"📱 Telefon raqam: <a href='tel: {phone}'>{phone}</a>\n\n"

        info += f"📝 Foydalanuvchining maqsadi:\n\n{message}"
        await bot.send_message(chat_id=admin, text=info, reply_markup=await confirm_no_confirm(user_id))
        await bot.session.close()


async def send_order_info(user_id, fullname, phone, project_type, project_tariff, message):
    await asyncio.sleep(5)
    for admin in ADMINS:
        info = f"📲 Buyurtma berish: \n"
        info += f"👤 Foydalanuvchining id raqami:   {user_id}\n\n"
        info += f"👤 Foydalanuvchining ismi:   {fullname}\n\n"
        info += f"📞 Foydalanuvchining telefon raqami:   <a href='tel:+998{phone}'>+998{phone}</a>\n\n"

        info += f"📃 Foydalanuvchining tanlagan loyihasi:   {project_type}\n\n"
        info += f"📄 Foydalanuvchining tanlagan tarifi:   {project_tariff}\n\n"
        info += f"📝 Foydalanuvchining maqsadi:\n\n{message}"
        await bot.send_message(chat_id=admin, text=info, reply_markup=await confirm_no_confirm(user_id))
        await bot.session.close()


async def send_order_info_full_phone(user_id, fullname, phone, project_type, project_tariff, message):
    await asyncio.sleep(5)
    for admin in ADMINS:
        info = f"📲 Buyurtma berish: \n"
        info += f"👤 Foydalanuvchining id raqami:   {user_id}\n\n"
        info += f"👤 Foydalanuvchining ismi:   {fullname}\n\n"
        info += f"📞 Foydalanuvchining telefon raqami:   <a href='tel:{phone}'>{phone}</a>\n\n"

        info += f"📃 Foydalanuvchining tanlagan loyihasi:   {project_type}\n\n"
        info += f"📄 Foydalanuvchining tanlagan tarifi:   {project_tariff}\n\n"
        info += f"📝 Foydalanuvchining maqsadi:\n\n{message}"
        await bot.send_message(chat_id=admin, text=info, reply_markup=await confirm_no_confirm(user_id))
        await bot.session.close()


@dp.callback_query(F.data.startswith('Kelishilgan_'))
async def update_data(call: CallbackQuery):
    user_id = call.data.split('_')[1]
    user_status = call.data.split('_')[0]
    call_message = call.message.text
    if 'Kontakt bilan bog\'lanish' in call_message:
        await db.update_contact_status(user_id, user_status)
        await call.message.answer("Foydalanuvchining malumoti muvaffaqiyatli ozgartirild!i")
        await call.message.delete()
    elif "Buyurtma berish" in call_message:
        await db.update_order_status(user_id, user_status)
        await call.message.answer("Foydalanuvchining malumoti muvaffaqiyatli ozgartirild!i")
        await call.message.delete()


@dp.callback_query(F.data.startswith('Rad etish_'))
async def update_data(call: CallbackQuery):
    user_id = call.data.split('_')[1]
    user_status = call.data.split('_')[0]
    call_message = call.message.text
    if 'Kontakt bilan bog\'lanish' in call_message:
        await db.update_contact_status(user_id, user_status)
        await call.message.answer("Foydalanuvchining malumoti muvaffaqiyatli ozgartirild!i")
        await call.message.delete()
    elif "Buyurtma berish" in call_message:
        await db.update_order_status(user_id, user_status)
        await call.message.answer("Foydalanuvchining malumoti muvaffaqiyatli ozgartirild!i")
        await call.message.delete()
