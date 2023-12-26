from aiogram import types
from Databases import filmsdatabase


# Инлайн клавиатура игры (левый/правый фильм)
def game_keyboard(user_num_of_films, k):
    buttons = [
        [types.InlineKeyboardButton(text="Меньше⬇", callback_data="film_left"),
         types.InlineKeyboardButton(text="Больше⬆", callback_data="film_right")
         ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


# Инлайн клавиатура следующего хода/завершения игры
def next_turn_keyboard():
    buttons = [
        [types.InlineKeyboardButton(text="Да", callback_data="next_turn"),
         types.InlineKeyboardButton(text="Завершить игру", callback_data="end_game")
         ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
