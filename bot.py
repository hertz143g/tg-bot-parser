from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters import Command
from parser import get_news
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "токен тут"

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📰 Новости")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выбери действие..."
)

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Привет! Нажми кнопку или введи команду.", reply_markup=keyboard)


@dp.message(Command("news"))
async def news_handler(message: Message):
    await message.answer("🔎 Собираю статьи...")
    for item in get_news():
        title, url = item
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🔗 Открыть статью", url=url)]
    ])
        await message.answer(f"🔹 {title}", reply_markup=keyboard)


@dp.message(lambda message: message.text == "📰 Новости")
async def handle_button_news(message: Message):
    await news_handler(message)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
