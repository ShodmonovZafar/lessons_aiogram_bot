import logging
from aiogram import Bot, Dispatcher, executor, types

from api_token import API_TOKEN
from constants import DESCRIPTION_COMMAND
from datas import count
import string
import random

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["description"])
async def description_command(message: types.Message):
    await message.answer(text=DESCRIPTION_COMMAND)
    await message.delete()

@dp.message_handler(commands=["count"])
async def count_command(message: types.Message):
    global count
    await message.answer(f"COUNT: {count}")
    count += 1

@dp.message_handler()
async def check_zero(message: types.Message):
    if "0" in message.text:
        return await message.reply("YES")
    await message.reply("NO")

@dp.message_handler()  # ASCII
async def send_random_letter(message: types.Message):
    await message.reply(random.choice(string.ascii_letters))

# Start the bot
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
