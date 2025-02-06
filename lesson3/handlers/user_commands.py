import random
from contextlib import suppress


from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import CallbackQuery, Message

from lesson3.keyboards import reply
from lesson3.keyboards.reply import main_kb

from aiogram import Router, Bot

router = Router()



@router.message(CommandStart())
async def start(message: Message):
    '''команда старт и клавиатура'''
    await message.answer('Hello people',
                         reply_markup=reply.main_kb)


@router.message(Command(commands=['rm', 'random-number']))
async def get_random_number(message: Message, command: CommandObject):
    '''Обрабатывает команды и выдает рандомное число'''
    a, b = [int(n) for n in command.args.split('-')]
    rnum = random.randint(a, b)
    await message.reply(f'Random number {rnum}')

@router.message(Command('test'))
async def test(message: Message, bot: Bot):
    await bot.send_message(message.chat.id, 'test')