from config import Config

import telegram

TELEGRAM_BOT_TOKEN = Config.TELEGRAM_BOT_TOKEN
TELEGRAM_DEFAULT_CHAT_ID = Config.TELEGRAM_DEFAULT_CHAT_ID

bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)


def send_message(message, chat_id=TELEGRAM_DEFAULT_CHAT_ID):
    """Send messages through telegram bot"""
    bot.send_message(chat_id, message)
