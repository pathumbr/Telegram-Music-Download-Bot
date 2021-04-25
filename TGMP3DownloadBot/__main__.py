# TG_MP3_Download_Bot

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from TGMP3DownloadBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from TGMP3DownloadBot import MP3DownloadBot as app
from TGMP3DownloadBot import LOGGER

pm_start_text = """
🎵 Telegram MP3 Download Bot 🎵

Hey [{}](tg://user?id={}) 👋 I'm Telegram MP3 Download Bot 🎵

Just Send me ✍️ The MP3 Name 👍 You Want to Download 👌
👀 Example: `/mp3 alone`

~ @mp3downloadtgbot 🎵
"""


@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="➕ Add Me to Your Group", url="t.me/mp3downloadtgbot?startgroup=true"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)
    add_chat_to_db(str(chat_id))


app.start()
LOGGER.info("TG MP3 Download Bot is online.")
idle()
