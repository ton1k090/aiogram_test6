from typing import Dict, Any, Callable, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message
from cachetools import TTLCache
from lesson3.keyboards.inline import sub_channel

'''Миддлеваре антифлуд для бота
В инит передается кол во секунд в течении которых сообщения будут игнорироваться'''


class AntiFloodMiddleware(BaseMiddleware):
    '''если в теч 2 секунд пользователь пишет комманду она просто не вызовется'''

    def __init__(self, time_limit: int=2):
        '''устанавливаем кол-во секунд для антифлуда'''
        self.limit = TTLCache(maxsize=10_000, ttl=time_limit)

    async def __call__(self,
                       handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
                       event: Message,
                       data: Dict[str, Any]
                       ):
        if event.chat.id in self.limit: # если отправлено в течении указаного лимита
            return
        else:
            self.limit[event.chat.id] = None
        return await handler(event, data)