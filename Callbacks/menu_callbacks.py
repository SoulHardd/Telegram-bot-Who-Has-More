from aiogram import Router, F, types
from Keyboards.menu_keyboards import menu_keyboard, close_button
from aiogram.enums import ParseMode
from Databases import userdatabase

router = Router()


@router.callback_query(F.data == "menu")
async def open_menu(callback: types.CallbackQuery):
    await callback.message.edit_reply_markup()
    await callback.message.answer(text="Меню:",
                                  reply_markup=menu_keyboard())


@router.callback_query(F.data == "close")
async def delete_msg(callback: types.CallbackQuery):
    await callback.message.edit_reply_markup()
    await callback.message.delete()


@router.callback_query(F.data == "rules")
async def rules(callback: types.CallbackQuery):
    await callback.message.answer(text='<strong>Правила игры "У кого больше?:"</strong>'
                            '\n\nВам предлагается два фильма из топа Кинопоиска,'
                            ' рейтинг первого <b>известен</b>.'
                            '\nЗадача состоит в том, чтобы угадать больше'
                            ' или меньше рейтинг второго фильма.'
                            '\n\nПри правильном ответе начисляется 1 балл, при неправильном - баллы обнуляются.'
                            '\nПосле каждого хода, вам откроются рейтинги обоих фильмов.'
                            '\n\nНабрав определенное количество баллов'
                            ' вы сможете попасть в топ игроков!'
                            '\n<strong>Удачи!</strong>',
                                  parse_mode=ParseMode.HTML,
                                  reply_markup=close_button())


@router.callback_query(F.data == "score")
async def user_score(callback: types.CallbackQuery):
    await callback.message.answer(text=f"Ваш максимальный счет:"
                                       f" {userdatabase.get_user_max_score(callback.from_user.id)}",
                                  reply_markup=close_button())


@router.callback_query(F.data == "top")
async def user_top(callback: types.CallbackQuery):
    await callback.message.answer(text=f'Топ игроков:\n'
                                       f'{userdatabase.get_top5_users()}',
                                  reply_markup=close_button())
