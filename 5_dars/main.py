import logging
from aiogram import Bot, Dispatcher, executor, types

from api_token import API_TOKEN
from constants import START_COMMAND
from stickers import ST1

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def on_startup(_):
    print("Bot launched successfully!")

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer(START_COMMAND, parse_mode="HTML")

@dp.message_handler(commands=["give"])
async def give_command(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker=ST1)
    await message.delete()

@dp.message_handler()
async def send_emoji(message: types.Message):
    await message.reply(message.text + "❤️ ")

# Start the bot
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    