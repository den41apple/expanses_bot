# -*- coding: utf-8 -*-
from aiogram import types

available_expanses_names = ['Такси', 'Развлечения', 'Продукты', 'Собака']
available_expanses_names_show = ['Такси', 'Развлечения', 'Продукты', 'Собака', 'Все расходы']


def expanses_types_keyboard(types_exp):
    kb = [types.KeyboardButton(text=item) for item in types_exp]
    return types.ReplyKeyboardMarkup(keyboard=[kb], resize_keyboard=True)


buttons = [
    [types.KeyboardButton(text='Показать расходы')],
    [types.KeyboardButton(text='Записать расходы')]
]

keyboard = types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
