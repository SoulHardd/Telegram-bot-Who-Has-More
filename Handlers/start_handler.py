from aiogram import Router, types
from aiogram.filters import Command
from aiogram.enums import ParseMode
from Keyboards.menu_keyboards import menu_keyboard
from Databases import userdatabase

router = Router()


# (Начало программы) Хэндлер для команды /start
@router.message(Command("start"))
async def cmd_start(message: types.Message):
    userdatabase.insert_user(message.from_user.id, message.from_user.username)
    await message.answer('<strong>Привет! Это игра "У кого больше?"</strong> '
                         '\nЕё смысл состоит в том,'
                         ' чтобы угадать у какого фильма больше рейтинг (<i>по мнению Кинопоиска</i>). '
                         '\n<b>Начнем игру?</b>',
                         parse_mode=ParseMode.HTML,
                         reply_markup=menu_keyboard()
                         )
