import os
import logging
from pyrogram import Client, __version__

BOT_TOKEN = os.environ.get("BOT_TOKEN")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class Bot(Client):
    def __init__(self):
        super().__init__(
            "My_Bot",
            bot_token=BOT_TOKEN,
            plugins=dict(root="plugins"),
            workers=100,
            sleep_threshold=5
        )
    async def start(self):
        await super().start()
        logging.info(f"{self.me.first_name} with Pyrogram v-{__version__} started on {self.me.username}.")

    async def stop(self, *args):
        await super().stop()
        logging.info("Bot stopped. Bye.")

Bot.run()
