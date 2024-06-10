import asyncio  # чтобы добавить асинхронную функцию main в цикл событий

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config  # чтобы задать настройки бота,с помощью файла .env


# Асинхронная функция конфигурирования и запуска бота
async def main() -> None:

    # Загружаем конфиг в переменную config
    # создаем объект config - экземпляр класса Config, через который
    # получаем доступ к токену бота.
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

# функция main асинхронная, поэтому мы не можем ее просто вызвать,
# как это делали с синхронными функциями -нужно запустить цикл событий и
# добавить функцию в него
asyncio.run(main())