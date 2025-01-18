from aiogram import types, filters, Router
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telegram_bot.database.connection import SessionLocal
from telegram_bot.database.models import User
from sqlalchemy.exc import OperationalError, IntegrityError

start_router = Router()


# TODO: дальше пользователь должен выбрать язык, который он хотел бы учить (под сообщением добавить кнопку выбрать язык и создать обработчик команды))

@start_router.message(filters.Command("start"))
async def message_start(message: types.Message):
    inline_bottom = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Выберите язык изучения", callback_data="/language_selection")]])
    try:
        with SessionLocal() as session:
            new_user = User(
                telegram_id=message.from_user.id,
                telegram_name=message.from_user.full_name,
                telegram_username=message.from_user.username
            )
            session.add(new_user)
            session.commit()
            await message.answer("Приветствую тебя, мой друг! Я буду твоим помощником в изучении нового языка."
                                 " Осталось выбрать какого именно.",
                                 reply_markup=inline_bottom)

    except IntegrityError:
        await message.answer("Вы уже зарегестрированы. Какой язык бы вы хотели повторить?",
                             reply_markup=inline_bottom)
    except OperationalError:
        await message.answer("Кажется я не смог связаться с базой данных")
    except Exception as e:
        await message.answer(f"Произошла ошибка {e} ")
