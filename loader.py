import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

import config
import handlers

logging.basicConfig(level=logging.INFO)
bot = Bot(config.TOKEN)
dp = Dispatcher()
dp.include_router(handlers.router)


def main():
    if config.WEBHOOK_TURN_ON:
        start_webhook()
    else:
        start_pooling()


def start_pooling():
    logging.info("START POOLING")
    loop = asyncio.get_event_loop()
    # Необходимо удалить веб хук
    loop.run_until_complete(bot.delete_webhook())
    loop.run_until_complete(dp.start_polling(bot))


def start_webhook():
    logging.info("START WEBHOOK")
    dp.startup.register(webhook_on_startup)
    app = web.Application()
    handler = SimpleRequestHandler(dispatcher=dp,
                                   bot=bot)
    handler.register(app, path=config.WEBHOOK_TELEGRAM_PATH)
    setup_application(app, dp, bot=bot)
    web.run_app(app,
                host=config.APP_HOST,
                port=config.APP_PORT)


async def webhook_on_startup(bot: Bot):
    """
    Установка веб хука
    """
    WEBHOOK_URL = config.WEBHOOK_TELEGRAM_URL + config.WEBHOOK_TELEGRAM_PATH
    kwargs = {}
    if config.WEBHOOK_SSL_CERT:
        kwargs.update(WEBHOOK_SSL_CERT=config.WEBHOOK_SSL_CERT)
    await bot.set_webhook(WEBHOOK_URL, **kwargs)


if __name__ == "__main__":
    main()
