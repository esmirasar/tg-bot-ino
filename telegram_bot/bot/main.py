import asyncio

from aiogram import Bot, Dispatcher

from config import config


bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()


async def on_start_up(dispatcher: Dispatcher) -> None:
    text = "Бот запущен"
    await bot.send_message(chat_id=config.ADMIN_ID, text=text)


async def main():
    from instruction_handler import start_router

    dp.include_router(start_router)

    await on_start_up(dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
