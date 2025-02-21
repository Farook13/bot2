import os
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_TOKEN, AUTH_CHANNEL, LOG_CHANNEL, OWNER_ID
from database import Database
from utils import check_force_sub

# Initialize the bot
app = Client("AutoFilterBot", bot_token=BOT_TOKEN)

# MongoDB instance
db = Database()

# Start command
@app.on_message(filters.command("start") & filters.private)
async def start(client: Client, message: Message):
    user_id = message.from_user.id
    # Check if user is subscribed
    if not await check_force_sub(client, user_id):
        await message.reply_text(
            "Please join our channel to use this bot!",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Join Channel", url=f"https://t.me/{AUTH_CHANNEL[4:]}")]]
            )
        )
        return
    
    await message.reply_text(
        "Welcome to the AutoFilter Bot! Send me a query to search for files."
    )
    # Log user activity
    await client.send_message(LOG_CHANNEL, f"User {user_id} started the bot.")

# Autofilter functionality
@app.on_message(filters.text & filters.private)
async def autofilter(client: Client, message: Message):
    user_id = message.from_user.id
    if not await check_force_sub(client, user_id):
        await message.reply_text(
            "Please join our channel to use this bot!",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Join Channel", url=f"https://t.me/{AUTH_CHANNEL[4:]}")]]
            )
        )
        return
    
    query = message.text
    results = db.search_files(query)
    if results:
        response = "Here are the files I found:\n\n"
        for idx, result in enumerate(results, 1):
            response += f"{idx}. {result['file_name']} - [Link]({result['file_link']})\n"
        await message.reply_text(response, disable_web_page_preview=True)
    else:
        await message.reply_text("No files found for your query.")

# Run the bot
if __name__ == "__main__":
    app.run()