from aiogram import Router, F, types
from Utils import extradefs
from Databases import userdatabase, filmsdatabase
from aiogram.utils.media_group import MediaGroupBuilder
from Keyboards import game_keyboards, start_keyboards, menu_keyboards


router = Router()


# Коллбэк при выборе фильма (верный/неверный ответ)
@router.callback_query(F.data.startswith("film_"))
async def game_callback(callback: types.CallbackQuery):
    await callback.message.edit_reply_markup()
    action = callback.data.split("_")[1]
    await callback.message.edit_text(f"Рейтинг фильма\n"
                                     f'"{filmsdatabase.get_film_name(userdatabase.get_film_list(callback.from_user.id)[userdatabase.get_current_counter(callback.from_user.id) + 1])}"'
                                     f" - # {filmsdatabase.get_film_rating(userdatabase.get_film_list(callback.from_user.id)[userdatabase.get_current_counter(callback.from_user.id)+1])}")
    if action == "left":
        if (int(userdatabase.get_film_list
                (callback.from_user.id)[userdatabase.get_current_counter(callback.from_user.id)])
                < int(userdatabase.get_film_list(callback.from_user.id)
                      [userdatabase.get_current_counter(callback.from_user.id) + 1])):
            userdatabase.update_current_score_and_counter(callback.from_user.id)
            await callback.message.answer(f"Верно! 😁  Твой счет:"
                                          f" {userdatabase.get_current_counter(callback.from_user.id)}"
                                          f"\nПродолжаем?",
                                          reply_markup=game_keyboards.next_turn_keyboard())
        else:
            await callback.message.answer("Неверно 😢")
            userdatabase.update_max_score(callback.from_user.id)
            await callback.message.answer(extradefs.end_score_message
                                          (userdatabase.get_current_counter(callback.from_user.id)),
                                          reply_markup=menu_keyboards.open_menu_button())
    if action == "right":
        if (int(userdatabase.get_film_list
                (callback.from_user.id)[userdatabase.get_current_counter(callback.from_user.id) + 1])
                < int(userdatabase.get_film_list(callback.from_user.id)
                      [userdatabase.get_current_counter(callback.from_user.id)])):
            userdatabase.update_current_score_and_counter(callback.from_user.id)
            await callback.message.answer(f"Верно! 😁  Твой счет:"
                                          f" {userdatabase.get_current_counter(callback.from_user.id)}"
                                          f"\nПродолжаем?",
                                          reply_markup=game_keyboards.next_turn_keyboard())
        else:
            await callback.message.answer("Неверно 😢")
            userdatabase.update_max_score(callback.from_user.id)
            await callback.message.answer(extradefs.end_score_message
                                          (userdatabase.get_current_counter(callback.from_user.id)),
                                          reply_markup=menu_keyboards.open_menu_button())


# Коллбэк при нажатии на кнопку следующего хода
@router.callback_query(F.data == "next_turn")
async def next_turn(callback: types.CallbackQuery):
    await callback.message.edit_reply_markup()
    await callback.message.answer('Отлично! Продолжаем')
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
                                  f" - # {filmsdatabase.get_film_rating(userdatabase.get_film_list(callback.from_user.id)[userdatabase.get_current_counter(callback.from_user.id)])}")
    await callback.message.answer(f"Рейтинг фильма\n"
                                  f'"{filmsdatabase.get_film_name(userdatabase.get_film_list(callback.from_user.id)[userdatabase.get_current_counter(callback.from_user.id)+1])}"'
                                  f"\nбольше или меньше?",
                                  reply_markup=game_keyboards.game_keyboard
                                  (userdatabase.get_film_list(callback.from_user.id),
                                   userdatabase.get_current_counter(callback.from_user.id)))
