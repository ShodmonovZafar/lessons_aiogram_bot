START_COMMAND = """
<em>Salom, botimizga <b>xush</b> kelibsiz! </em>"""

DARS_3 = """
```
import logging
from aiogram import Bot, Dispatcher, executor, types

from api_token import API_TOKEN
from constants import HELP_COMMAND, START_COMMAND

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer(START_COMMAND)
    await message.delete()

# Start the bot
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
```
"""