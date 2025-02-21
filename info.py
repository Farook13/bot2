import os

# Telegram Bot Token from @BotFather
BOT_TOKEN = os.getenv("BOT_TOKEN")

# MongoDB Configuration
DATABASE_URI = os.getenv("DATABASE_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME", "AutoFilterBotDB")

# Force Subscribe Channel ID (e.g., -100123456789)
AUTH_CHANNEL = os.getenv("AUTH_CHANNEL")

# Log Channel ID for bot activities
LOG_CHANNEL = os.getenv("LOG_CHANNEL")

# Bot Owner ID
OWNER_ID = int(os.getenv("OWNER_ID", "123456789"))