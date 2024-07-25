import os
import django
from aiogram.fsm.context import FSMContext

from posts.models import Project_Type, Tariff

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from keyboards.inline import orders_status, orders_users
from aiogram import F, types
from aiogram.types import CallbackQuery
from loader import db, dp
from states import OrderState
from asgiref.sync import sync_to_async

statues = ('Ariza yuborilgan', 'Rad etish', 'Qabul qilingan', 'Kelishilgan', 'Kelishilmagan', 'Davom etayotgan proyekt',
           'Tugatilgan proyekt')


@dp.message(F.text == 'Buyurtmalarni korish')
async def send_orders(msg: types.Message, state: FSMContext):
    # orders_ids = await db.get_orders_ids()
    # if orders_ids:
        await msg.answer("Kormoqchi bo'lgan foydalanuvchining id sini tanlang:", reply_markup=await orders_users())
        await state.set_state(OrderState.order_user)
    # else:
        await msg.answer("Buyurtmalar hali mavjud emas!")
        await state.clear()


@dp.callback_query(F.data.endswith('foydalanuvchi'), OrderState.order_user)
async def get_orders(call: CallbackQuery, state: FSMContext):
    user_id = call.data.split('-')[0]
    order_user = await db.get_order_from_id(user_id)
    project_type = await sync_to_async(Project_Type.objects.get)(pk=order_user[5])
    project_tariff = await sync_to_async(Tariff.objects.get)(pk=order_user[6])
    info = f"📲 Buyurtma berish: \n"
    info += f"👤 Foydalanuvchining id raqami:   {user_id}\n\n"
    info += f"👤 Foydalanuvchining ismi:   {order_user[1]}\n\n"

    if '+998' in order_user[2]:
        info += f"📱 Telefon raqam: <a href='tel: {order_user[2]}'>{order_user[2]}</a>\n\n"
    else:
        info += f"📱 Telefon raqam: <a href='tel: +998{order_user[2]}'>+998{order_user[2]}</a>\n\n"

    info += f"📃 Foydalanuvchining tanlagan loyihasi:   {project_type.title}\n\n"
    info += f"📄 Foydalanuvchining tanlagan tarifi:   {project_tariff.title}\n\n"
    info += f"📝 Foydalanuvchining maqsadi:\n\n{order_user[3]}"
    await call.message.answer(f"{info}", reply_markup=await orders_status(user_id))
    await state.set_state(OrderState.order_update)
    await call.message.delete()


@dp.callback_query(F.data.startswith(statues), OrderState.order_update)
async def update_order(call: CallbackQuery, state: FSMContext):
    user_id = call.data.split('-')[1]
    user_status = call.data.split('-')[0]
    await db.update_order_status(user_id, user_status)
    await call.message.answer("Foydalanuvchi malumoti muvaffaqiyatli ozgartirildi!")
    await state.clear()
    await call.message.delete()
