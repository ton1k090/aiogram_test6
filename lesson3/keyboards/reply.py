from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

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