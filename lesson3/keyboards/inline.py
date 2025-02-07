from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

links_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='youtube', url='https://youtube.com'),
            InlineKeyboardButton(text='telegram', url='tg://resolve?domain=CrComatoz'),
        ],
    ]
)

sub_channel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='subscribe', url='https://t.me/cmtz')
        ]
    ]
)