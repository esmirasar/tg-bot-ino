from aiogram import types, filters, Router


start_router = Router()


@start_router.message(filters.Command("start"))
async def message_start(message: types.Message):
    print(message.from_user)
    await message.answer("Бот запущен")


