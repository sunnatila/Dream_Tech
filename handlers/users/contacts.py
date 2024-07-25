import os
import django
from aiogram.fsm.context import FSMContext

from keyboards.inline import contacts_users, contacts_status

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from aiogram import F, types
from aiogram.types import CallbackQuery
from loader import db, dp
from states import ContactState

statues = ('Kontakt yuborilgan', 'Rad etish', 'Xabar o\'qildi', 'Kelishilgan', 'Zakaz olingan', 'Javob berilgan')


@dp.message(F.text == 'Kontaktlarni korish')
async def send_contacts(msg: types.Message, state: FSMContext):
    contact_ids = await db.get_contacts_ids()
    if contact_ids:
        await msg.answer("Kormoqchi bo'lgan foydalanuvchining id sini tanlang:", reply_markup=await contacts_users())
        await state.set_state(ContactState.contact_user)
    else:
        await msg.answer("Kontaktlar hali mavjud emas!")
        await state.clear()


@dp.callback_query(F.data.endswith('foydalanuvchi'), ContactState.contact_user)
async def get_contacts(call: CallbackQuery, state: FSMContext):
    user_id = call.data.split('-')[0]
    contact_user = await db.get_contact_from_id(user_id)
    info = f"📞 Kontakt bilan bog'lanish:\n"
    info += f"👤 Foydalanuvchining ismi:   {contact_user[1]}\n\n"
    if '+998' in contact_user[2]:
        info += f"📱 Telefon raqam: <a href='tel: {contact_user[2]}'>{contact_user[2]}</a>\n\n"
    else:
        info += f"📱 Telefon raqam: <a href='tel: +998{contact_user[2]}'>+998{contact_user[2]}</a>\n\n"

    info += f"📝 Foydalanuvchining maqsadi:\n\n{contact_user[3]}"
    await call.message.answer(f"{info}", reply_markup=await contacts_status(user_id))
    await state.set_state(ContactState.contact_update)
    await call.message.delete()


@dp.callback_query(F.data.startswith(statues), ContactState.contact_update)
async def update_contact(call: CallbackQuery, state: FSMContext):
    user_id = call.data.split('-')[1]
    user_status = call.data.split('-')[0]
    await db.update_contact_status(user_id, user_status)
    await call.message.answer("Foydalanuvchi malumoti muvaffaqiyatli ozgartirildi!")
    await state.clear()
    await call.message.delete()
