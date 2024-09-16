from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from src.database.config import settings
from src.bot.haldlers.doctor import register as register_doctor
from src.bot.haldlers.doctor import command_register as command_register_doctor


class Webhook:
    def __init__(self):
        self.bot = Bot(token=settings.token_telegram_bot)
        self.dp = Dispatcher(storage=MemoryStorage())

    async def register_handler(self):
        await register_doctor(self.dp)
        await command_register_doctor(self.bot)

    async def create(self):
        print('[ONLINE]')
        await self.bot.delete_webhook(drop_pending_updates=True)
        await self.register_handler()
        await self.dp.start_polling(self.bot)

    @staticmethod
    async def delete():
        print('GoodBye')
