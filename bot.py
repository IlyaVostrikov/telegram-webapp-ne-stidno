from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
import asyncio

# Токен Telegram-бота
BOT_TOKEN = "8225464968:AAGzQO0JqRGVwxMczrHBancRLxDRdXfgV_I"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="📲 Открыть меню",
            web_app=WebAppInfo(url="https://telegram-webapp-ne-stidno.vercel.app")
        )]
    ])
    await message.answer("Привет! Нажми кнопку ниже, чтобы открыть меню ☕", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        input("Нажмите Enter для выхода...")
