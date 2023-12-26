import asyncio
import logging
from aiogram import Bot, Dispatcher

import Utils.extradefs
from Handlers import start_handler
from Properties.token import token
from Callbacks import start_end_call, game_calls, menu_callbacks
from Databases import userdatabase, filmsdatabase


logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)
dp = Dispatcher()


async def main():
    userdatabase.init_udb()
    filmsdatabase.init_fdb()
    userdatabase.udb_start()
    Utils.extradefs.make_list_films()
    dp.include_router(start_handler.router)
    dp.include_router(start_end_call.router)
    dp.include_router(game_calls.router)
    dp.include_router(menu_callbacks.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    finally:
        userdatabase.close_udb()
        filmsdatabase.close_fdb()
