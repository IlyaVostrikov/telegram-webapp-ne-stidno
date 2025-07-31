from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router
import asyncio

from handlers import classic_menu

# Токен Telegram-бота
BOT_TOKEN = "8225464968:AAGzQO0JqRGVwxMczrHBancRLxDRdXfgV_I"

# Создаем бота и диспетчер
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Создаем роутер и подключаем обработчики
app = Router()
app.include_router(classic_menu.router)
dp.include_router(app)

# Хендлер для старта
@dp.message()
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="📲 Открыть меню",
            web_app=WebAppInfo(url="https://telegram-webapp-ne-stidno.vercel.app")
        )]
    ])
    await message.answer("Привет! Нажми кнопку ниже, чтобы открыть меню ☕", reply_markup=keyboard)

# Точка входа
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        input("Нажмите Enter для выхода...")
