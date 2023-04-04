import logging
from aiogram import Bot, Dispatcher, executor, types

from api_token import API_TOKEN
from constants import GIVE_COMMAND, HELP_COMMAND
from stickers import STICKER1

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def on_startup(_):
    print("Men boshladim!")

@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await message.answer(HELP_COMMAND, parse_mode="HTML")

@dp.message_handler(content_types=["sticker"])
async def send_sticker_id(message: types.Message):
    await message.answer(message.sticker.file_id)
    await bot.send_sticker(message.from_user.id, sticker=STICKER1)

# @dp.message_handler()
# async def count(message: types.Message):
#     await message.answer(text=str(message.text.count("✅")))

# @dp.message_handler(commands=["give"])
# async def give_command(message: types.Message):
#     await message.answer(GIVE_COMMAND)
#     await bot.send_sticker(message.from_user.id, sticker=STICKER1)

# @dp.message_handler()
# async def echo(message: types.Message):
#     if message.text == "❤️":
#         await message.answer("🖤")

# Start the bot
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
