from pyrogram import Client, filters
from info import BOT_TOKEN, OWNER_ID

app = Client("AutoFilterBot", bot_token=BOT_TOKEN)

@app.on_message(filters.command("intro") & filters.private)
async def intro(client: Client, message: Message):
    intro_text = (
        "Hello! I am an AutoFilter Bot created to help you find files quickly.\n\n"
        "Features:\n"
        "- Search files from a MongoDB database.\n"
        "- Force subscribe to access bot features.\n"
        "- Utility options for a smooth experience.\n\n"
        f"My creator is a cool person with Telegram ID:@Faroo_bruh . "
        "Say hi to them if you get a chance!"
    )
    await message.reply_text(intro_text)

if __name__ == "__main__":
    app.run()