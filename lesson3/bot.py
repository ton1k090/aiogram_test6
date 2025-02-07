import asyncio
from aiogram import Bot, Dispatcher
from handlers import bot_messages, user_commands, questionaire
from callback import pagination
from config_reader import config
from lesson3.middlewares.antiflood import AntiFloodMiddleware
from lesson3.middlewares.check_sub import CheckSubscription


async def main():
    bot = Bot(config.bot_token.get_secret_value()) # Передать токен нужного бота
    dp = Dispatcher() # создать диспетчер - обработчик событий
    # dp.message.middleware(CheckSubscription()) # зарегестрировать мидлвеар
    dp.message.middleware(AntiFloodMiddleware())
    dp.include_routers(                # зарегестрировать роуты
        user_commands.router,
        pagination.router,
        questionaire.router,
        bot_messages.router

    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot) # отлавливать апдейты


if __name__ == '__main__':
    asyncio.run(main()) # запустить бота