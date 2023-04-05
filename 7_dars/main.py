import logging
from aiogram import Bot, Dispatcher, executor, types

from api_token import API_TOKEN
from constants import HELP_COMMAND
from links_to_photos import PHOTO1

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    # await message.answer(message.text)
    # await bot.send_message(chat_id=message.from_user.id,
    #                       text="Hello")
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode="HTML")
    await message.delete()

@dp.message_handler(commands=["photo"])
async def send_photo(messege: types.Message):
    await bot.send_photo(chat_id=messege.chat.id,
                         photo=PHOTO1)
    await messege.delete()

@dp.message_handler(commands=["location"])
async def send_location(messege: types.Message):
    await bot.send_location(chat_id=messege.from_user.id,
                         latitude=55,
                         longitude=74)
    await messege.delete()

# Start the bot
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
