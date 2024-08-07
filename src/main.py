import sys
sys.dont_write_bytecode = True

import asyncio

from aiogram import Bot
from loguru import logger

from bot.dispatcher import get_dispatcher
from bot.structures.data_structure import TransferData
from config import settings
from db.database import create_async_engine


async def app():

    bot = Bot(token=settings.bot.BOT_TOKEN)
    dp = get_dispatcher() 

    async_engine = create_async_engine(
        url=settings.db.create_connection_url(),
        echo=True
    )
    
    await dp.start_polling(bot, **TransferData(engine=async_engine))


def main():

    try:
        logger.warning('Bot was starting')
        asyncio.run(app())

    except (KeyboardInterrupt, SystemExit):
        logger.warning('Bot was stopping')


if __name__ == '__main__':
    main()
