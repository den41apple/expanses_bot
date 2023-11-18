# -*- coding: utf-8 -*-
from aiogram import F, Router
from aiogram import types
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from database import register, approve_user, \
    new_expanse, show_my_id, show_expanses

from keyboards import keyboard, expanses_types_keyboard,\
    available_expanses_names, available_expanses_names_show
from fsm import States, ShowStates


router = Router()


@router.message(Command("reg"))
async def new_user(message: types.Message):
    reg = register(message.from_user.id, message.from_user.first_name)
    await message.answer(f'{reg}\n'
                         f'Используйте команду /start снова, чтобы начать')


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    if approve_user(message.from_user.id):
        await message.answer(f'Привет, {message.from_user.first_name}\n'
                             f'Используй клавиатуру ниже, а также: '
                             f'доступные команды:\n'
                             f'/myid\n',
                             reply_markup=keyboard)
    else:
        await message.answer('Нет доступа к боту расходов\n'
                             'Вам необходимо зарегистрироваться командой /reg')


@router.message(Command("myid"))
async def my_id(message: types.Message):
    id = show_my_id(message.from_user.id)
    await message.answer(f'Твой id: {id}\n'
                         f'поделись им с другом, чтобы он посмотрел твои расходы')


# @dp.message(F.text.lower() == "показать расходы")
@router.message(F.text.lower() == "показать расходы")
async def show_user_expanses(message: types.Message, state: FSMContext):
    await message.answer(f'Какой тип расходов вы хотите посмотреть?',
                         reply_markup=expanses_types_keyboard(available_expanses_names_show)
                         )
    await state.set_state(ShowStates.show_ex)


# @dp.message(ShowStates.show_ex)
@router.message(ShowStates.show_ex)
async def choosen_type_expanses(message: types.Message, state: FSMContext):
    await state.update_data(expanse_type_name=message.text)
    await message.answer(f'Вы выбрали {message.text}\n'
                         f'Теперь введите количество дней цифрой/числом за которое хотите посмотреть',
                         reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(ShowStates.count_days)


# @dp.message(ShowStates.count_days)
@router.message(ShowStates.count_days)
async def choosen_days_expanses(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    x = show_expanses(message.from_user.id,
                      user_data['expanse_type_name'],
                      int(message.text))
    await message.answer(f'За {user_data["expanse_type_name"]} вы отдали {x}\n'
                         f'Чтобы посмотреть или записать что-то еще нажмите на команду /start')
    await state.clear()


# @dp.message(F.text.lower() == 'записать расходы')
@router.message(F.text.lower() == "записать расходы")
async def new_expanses(message: types.Message, state: FSMContext):
    await message.answer('Введите тип расходов',
                         reply_markup=expanses_types_keyboard(available_expanses_names)
                         )
    await state.set_state(States.expanse_name)


# @dp.message(States.expanse_name)
@router.message(States.expanse_name)
async def add_expanse(message: types.Message, state: FSMContext):
    await state.update_data(add_expanse_name=message.text)
    await message.answer(f'Введите сумму которую потратили:',
                         reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(States.expanse_cost)


# @dp.message(States.expanse_cost)
@router.message(States.expanse_cost)
async def feedback_add_expanse(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    new_expanse(user_data['add_expanse_name'], message.text, message.from_user.id)
    await message.answer(f'Вы добавили в ваш дневник: {message.text}рублей за {user_data["add_expanse_name"]}\n'
                         f'Чтобы посмотреть или записать что-то еще нажмите на команду /start',
                         reply_markup=types.ReplyKeyboardRemove())
    await state.clear()
