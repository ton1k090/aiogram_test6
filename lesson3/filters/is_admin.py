from typing import List
from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsAdmin(BaseFilter):
    '''Класс проверяет на админа, админ передается в инит'''
    def __init__(self, user_ids: int | List[int]):
        self.user_ids = user_ids

    def __call__(self, message: Message):
        if isinstance(self.user_ids, int):
            return message.from_user.id == self.user_ids
        return message.from_user.id in self.user_ids