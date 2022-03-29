from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Client.on_message(filters.command(["start", "start@ChannelBanRobot"]))
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>
 `Heya I'm A Anti Channel Tegram bot to delete and ban message sent by channel`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📢 Cʜᴀɴɴᴇʟ", url="https://t.me/x_ro_bots"
                    ),
                    InlineKeyboardButton(
                        "Sᴜᴅᴏ �", url="https://t.me/yukurima"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧑‍💻 Dᴇᴠ 🧑‍💻", url="https://t.me/JawRipper"
                    )
                ]
            ]
        )
    )
