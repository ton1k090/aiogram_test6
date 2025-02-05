from aiogram.types import (
    ReplyKeyboardMarkup,    # крепится под полем ввода
    KeyboardButton,         # кнопки для клавиатуры
    InlineKeyboardButton,   #  кнопки
    InlineKeyboardMarkup,
    KeyboardButtonPollType# крепится под сообщениями
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, \
    InlineKeyboardBuilder  # если много кнопок лучше использовать его
from aiogram.filters.callback_data import CallbackData


main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='smiles'),
            KeyboardButton(text='links')
        ],
        [
            KeyboardButton(text='calculate'),
            KeyboardButton(text='special buttons')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True, # наша клавиатура будет скрываться после первого нажатия
    input_field_placeholder='select a menu item',
    selective=True # клавиатура активируется только у того кто ее вызвал - для чатов
)

links_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='youtube', url='https://youtube.com'),
            InlineKeyboardButton(text='telegram', url='tg://resolve?domain=CrComatoz'),
        ],
    ]
)


spec_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='send geo', request_location=True),
            KeyboardButton(text='send contact', request_contact=True),
            KeyboardButton(text='create a survey', request_poll=KeyboardButtonPollType()) # Создать викторину голосоыание опрос
        ],
        [
            KeyboardButton(text='back')
        ]
    ],
    resize_keyboard=True
)


class Pagination(CallbackData, prefix='pag'):
    action: str
    page: int


def paginator(page: int=0):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='⬅️', callback_data=Pagination(action='prev', page=page).pack()),
        InlineKeyboardButton(text='➡️', callback_data=Pagination(action='next', page=page).pack()),
        width=2
    )
    return builder.as_markup()



def calc_cb():
    items = [
        '1', '2', '3', '/',
        '4', '5', '6', '*',
        '7', '8', '9', '-',
        '0', '.', '=', '+'
    ]
    builder = ReplyKeyboardBuilder()
    [builder.button(text=item) for item in items]
    builder.button(text='back')
    builder.adjust(*[4] * 4) # сколько кнопок на одном ряду

    return builder.as_markup(resize_keyboard=True)