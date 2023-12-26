from aiogram import types


def open_menu_button():
    button = [[
        types.InlineKeyboardButton(text="Начать сначала", callback_data="restart"),
        types.InlineKeyboardButton(text="Открыть меню", callback_data="menu")
    ]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button)
    return keyboard


def close_button():
    button = [[
        types.InlineKeyboardButton(text="Закрыть", callback_data="close")
    ]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button)
    return keyboard


def menu_keyboard():
    buttons = [
        [
            types.InlineKeyboardButton(text="Играть", callback_data="menustart"),
            types.InlineKeyboardButton(text="Правила игры", callback_data="rules")
        ],
        [types.InlineKeyboardButton(text="Посмотреть максимальный счет", callback_data="score")],
        [types.InlineKeyboardButton(text="Топ игроков", callback_data="top")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
