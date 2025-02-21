import os

# Telegram Bot Token from @BotFather
BOT_TOKEN = os.getenv("7857321740:AAEtcoE9BbLGCaF5TlkeGvhLZpXU36vco8E")

# Telegram API ID and Hash from my.telegram.org
API_ID = int(os.getenv("12618934"))
API_HASH = os.getenv("49aacd0bc2f8924add29fb02e20c8a16")
# MongoDB Configuration
DATABASE_URI = os.getenv("mongodb+srv: //farook:farook@cluster0.dmaou.mongodb.net/")
DATABASE_NAME = os.getenv("DATABASE_NAME", "Farook")

# Force Subscribe Channel ID (e.g., -100123456789)
AUTH_CHANNEL = os.getenv("-1002256041072")

# Log Channel ID for bot activities
LOG_CHANNEL = os.getenv("-1002467149516")

# Bot Owner ID
OWNER_ID = int(os.getenv("OWNER_ID", "5032034594"))