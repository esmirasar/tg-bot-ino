from aiogram import types, filters, Router

from telegram_bot.database.connection import SessionLocal
from telegram_bot.database.models import User

start_router = Router()
# TODO: при повторной отправке старт, выводится ошибка, что пользователь есть

@start_router.message(filters.Command("start"))
async def message_start(message: types.Message):
    with SessionLocal() as session:
        user = session.get(User, message.from_user.id)
        if not user:
            new_user = User(
                telegram_id=message.from_user.id,
                telegram_name=message.from_user.full_name,
                telegram_username=message.from_user.username
            )
            session.add(new_user)
            session.commit()

        await message.answer("Приветствую тебя, мой друг! Я буду твоим помощником в изучении нового языка."
                             " Осталось выбрать какого именно.")


