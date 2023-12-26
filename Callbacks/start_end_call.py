from aiogram import Router, F, types
from Utils import extradefs
from Databases import userdatabase, filmsdatabase
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder
from Keyboards import game_keyboards, start_keyboards, menu_keyboards


router = Router()


# Коллбэк при старте и рестарте игры
@router.callback_query(F.data.endswith("start"))
async def start_game(callback: types.CallbackQuery):
    userdatabase.nullification_of_temp_data(callback.from_user.id)
    extradefs.shuffle_list_of_films(callback.from_user.id)
    await callback.message.edit_reply_markup()
    if callback.data == "menustart":
        await callback.message.delete()
    await callback.message.answer('Отлично! Начинаем')
    album_builder = MediaGroupBuilder()
    album_builder.add_photo(media=filmsdatabase.get_film_poster_url
                            (userdatabase.get_film_list(callback.from_user.id)
                             [userdatabase.get_current_counter(callback.from_user.id)]))
    album_builder.add_photo(media=filmsdatabase.get_film_poster_url
                            (userdatabase.get_film_list(callback.from_user.id)
                             [userdatabase.get_current_counter(callback.from_user.id) + 1]))
    await callback.message.answer_media_group(media=album_builder.build())
    await callback.message.answer(f"Рейтинг фильма\n"
                                  f'"{filmsdatabase.get_film_name(userdatabase.get_film_list(callback.from_user.id)[userdatabase.get_current_counter(callback.from_user.id)])}"'
                                  f" - {userdatabase.get_film_list(callback.from_user.id)[userdatabase.get_current_counter(callback.from_user.id)]}"
                                  f"\n(🔝{filmsdatabase.get_film_rating(userdatabase.get_film_list(callback.from_user.id)[userdatabase.get_current_counter(callback.from_user.id)])})")
    await callback.message.answer(f"Рейтинг фильма\n"
                                  f'"{filmsdatabase.get_film_name(userdatabase.get_film_list(callback.from_user.id)[userdatabase.get_current_counter(callback.from_user.id) + 1])}"'
                                  f"\nбольше или меньше?",
                                  reply_markup=game_keyboards.game_keyboard
                                  (userdatabase.get_film_list(callback.from_user.id),
                                   userdatabase.get_current_counter(callback.from_user.id)))


# Коллбэк при нажатии на кнопку окончания игры
@router.callback_query(F.data == "end_game")
async def end_game(callback: types.CallbackQuery):
    userdatabase.update_max_score(callback.from_user.id)
    await callback.message.edit_reply_markup()
    await callback.message.answer(extradefs.end_score_message(userdatabase.get_current_score(callback.from_user.id)),
                                  reply_markup=menu_keyboards.open_menu_button())
