from config import Config
from slack_sdk import WebClient

SLACK_BOT_TOKEN = Config.SLACK_BOT_TOKEN
SLACK_DEFAULT_CHANNEL = Config.SLACK_DEFAULT_CHANNEL

client = WebClient(token=SLACK_BOT_TOKEN)


def send_message(message, channel=SLACK_DEFAULT_CHANNEL):
    """Send messages through Slack bot"""
    client.chat_postMessage(channel=channel, text=message)
