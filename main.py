import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers import router

load_dotenv()

dp = Dispatcher()

bot = Bot(os.environ['BOT_API'])


async def main() -> None:
    dp.include_router(router)
    await dp.start_polling(bot)


# Основная точка входа
if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO,
                        stream=sys.stdout)  # Можно настроить вывод в консоль
                        # filename='log.txt', encoding='utf-8')  # Логи сохраняются в файл
    asyncio.run(main())
