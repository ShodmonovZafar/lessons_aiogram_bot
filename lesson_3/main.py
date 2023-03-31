import logging
from aiogram import Bot, Dispatcher, executor, types

from api_token import API_TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Start the bot
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)