from aiogram import F
from aiogram.types import Message

from lesson3.data.subloader import get_json
from lesson3.keyboards import reply, builders, fabrics
from lesson3.keyboards.inline import links_kb
from lesson3.keyboards.reply import main_kb
from aiogram import Router

router = Router()

@router.message(F.text.lower().in_({'привет', 'хай'}))
async def greeting(message: Message):
    '''если ввести что то из этого списка последует ответ'''
    await message.reply('Привет')


@router.message(F.text == 'back')
async def back(message: Message):
    '''кнопка назад'''
    await message.answer('back', reply_markup=main_kb)


@router.message()
async def echo(message: Message):
    '''обработчик кнопок главного меню'''
    msg = message.text.lower()
    smiles = await get_json('smiles.json')
    if msg == 'links':
        await message.answer('here are your links',
                             reply_markup=links_kb)
    elif msg == 'special buttons':
        await message.answer('special buttons', reply_markup=reply.spec_kb)
    elif msg == 'calculate':
        await message.answer(text='enter the expression', reply_markup=builders.calc_cb())
    elif msg == 'smiles':
        await message.answer(text=f'{smiles[0][0]} {smiles[0][1]}',
                             reply_markup=fabrics.paginator())