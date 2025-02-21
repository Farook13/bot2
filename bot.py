from pyrogram import Client, filters
from config import Config
from handlers import start, filter, admin

class AutoFilterBot(Client):
    def __init__(self):
        super().__init__(
            "AutoFilterBot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN
        )
        self._register_handlers()

    def _register_handlers(self):
        """Register all message handlers."""
        @self.on_message(filters.command("start"))
        async def start_cmd(client, message):
            await start.start_command(client, message)

        @self.on_message(filters.text & ~filters.command(["start", "add", "delete"]))
        async def filter_cmd(client, message):
            await filter.filter_handler(client, message)

        @self.on_message(filters.command("add"))
        async def add_file_cmd(client, message):
            await admin.add_file(client, message)

        @self.on_message(filters.command("delete"))
        async def delete_file_cmd(client, message):
            await admin.delete_file(client, message)

    def start_bot(self):
        """Start the bot."""
        print("Bot starting...")
        self.run()

# Singleton instance
bot_instance = AutoFilterBot()