from telebot.async_telebot import AsyncTeleBot

TOKEN = '5820204529:AAHigN5yIQBGSgOG7NSM4l93sGppL5J2AR4'
bot = AsyncTeleBot(TOKEN)

from handlers import *
from modules import GameManager

manager = GameManager()

if __name__ == '__main__':
    asyncio.run(bot.polling(non_stop=True))
