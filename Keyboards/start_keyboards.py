from aiogram import types


def start_button():
    button = [[
        types.InlineKeyboardButton(text="Начать игру",
                                   callback_data="start")
    ]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button)
    return keyboard


def restart_button():
    button = [[
        types.InlineKeyboardButton(text="Начать сначала",
                                   callback_data="restart")
        ]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button)
    return keyboard
