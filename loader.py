from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage


from data import config
from utils.db_api import Database

bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
db = Database()


async def main_connector():
    await db.connector()
