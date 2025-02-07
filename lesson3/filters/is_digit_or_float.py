from aiogram.filters import BaseFilter, CommandObject
from aiogram.types import Message
from typing import Any


class CheckForDigit(BaseFilter):
    '''Класс проверяет что введены только цифры
    инт либо флоат'''
    async def __call__(self, message: Message, **data: Any):
        command: CommandObject = data.get('command')
        arg = command.args
        if arg.isnumeric() or (arg.count('.') == 1 and arg.replace('.', '').isnumeric()):
            return True
        return False


