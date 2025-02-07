'''проверять подписку на канал чтобы пользоваться ботом'''
from typing import Dict, Any, Callable, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message

from lesson3.keyboards.inline import sub_channel


class CheckSubscription(BaseMiddleware):
    async def __call__(self,
                       handler : Callable[[Message,
                        Dict[str, Any]],
                        Awaitable[Any]],
                        event: Message, data: Dict[str, Any]):
        chat_member = await event.bot.get_chat_member('@cmtz', event.from_user.id)
        if chat_member.status == 'left':
            await event.answer('subscribe to chanel', reply_markup=sub_channel)
        else:
            return await handler(event, data)
