import os

from dotenv import load_dotenv

load_dotenv()


class BotConfig:
    BOT_TOKEN = os.getenv('BOT_TOKEN')

    ADMIN_ID = os.getenv('ADMIN_ID')

config = BotConfig()
