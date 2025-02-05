import asyncio
import random
from contextlib import suppress
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.exceptions import TelegramBadRequest
from lesson2 import keyboards
from lesson2.keyboards import main_kb, links_kb, spec_kb, calc_cb, paginator

bot = Bot('7856567344:AAEgAgghZ40M9H71MpaDK7_ELR5SlqszZe0')
dp = Dispatcher()

smiles = [
    ['😀', 'lol'],
    ['😊', 'smile'],
    ['😞', 'sadness'],
    ['😇', 'angel'],
]


@dp.message(CommandStart())
async def start(message: Message):
    '''команда старт и клавиатура'''
    await message.answer('Hello people',
                         reply_markup=main_kb)


@dp.callback_query(keyboards.Pagination.filter(F.action.in_(['prev', 'next'])))
async def pagination_filter(call: CallbackQuery, callback_data: keyboards.Pagination):
    page_num = int(callback_data.page)
    page = page_num - 1 if page_num > 0 else 0

    if callback_data.action == 'next':
        page = page_num + 1 if page_num < (len(smiles) - 1) else page_num

    with suppress(TelegramBadRequest):
        await call.message.edit_text(
            f'{smiles[page][0]} {smiles[page][1]}',
            reply_markup=keyboards.paginator(page)
        )
    await call.answer()


@dp.message(F.text.lower().in_({'привет', 'хай'}))
async def greeting(message: Message):
    '''если ввести что то из этого списка последует ответ'''
    await message.reply('Привет')


@dp.message(F.text == 'back')
async def back(message: Message):
    '''кнопка назад'''
    await message.answer('back', reply_markup=main_kb)


@dp.message()
async def echo(message: Message):
    '''обработчик кнопок главного меню'''
    msg = message.text.lower()
    if msg == 'links':
        await message.answer('here are your links',
                             reply_markup=links_kb)
    elif msg == 'special buttons':
        await message.answer('special buttons', reply_markup=spec_kb)
    elif msg == 'calculate':
        await message.answer(text='enter the expression', reply_markup=calc_cb())
    elif msg == 'smiles':
        await message.answer(text=f'{smiles[0][0]} {smiles[0][1]}',
                             reply_markup=paginator())


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())