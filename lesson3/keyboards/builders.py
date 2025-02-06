from aiogram.utils.keyboard import ReplyKeyboardBuilder


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