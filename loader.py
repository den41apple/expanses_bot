import os
from dotenv import load_dotenv
import logging
from aiogram import Bot, Dispatcher

import handlers
import asyncio
import handlers
# from handlers import new_user


async def main():
    load_dotenv()

    logging.basicConfig(level=logging.INFO)

    bot = Bot(os.getenv('TOKEN'))

    dp = Dispatcher()
    dp.include_router(handlers.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

