import asyncio 
import logging 
import sys
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties 
from aiogram.enums import ParseMode 
from aiogram. filters import CommandStart 
from aiogram.types import Message
from async_mistral import main_mistral

TOKEN = "8180132074:AAFxr6oCd8KTtW87Equyc0V-K6urqSR9sJ4"

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}")

@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        content = message.text
        res = await main_mistral(content)
        await message.answer(res)


    except TypeError:
        await message.answer("Nice try")

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
