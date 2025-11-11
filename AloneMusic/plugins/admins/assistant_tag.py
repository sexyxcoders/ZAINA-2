import asyncio
from pyrogram import filters
from pyrogram.enums import ParseMode
from AloneMusic import app
from AloneMusic.assistant_client import assistant
from AloneMusic.utils.Tnc_checker import admins_check

# Keep track of chats where tagging is active
SPAM_CHATS = []

# ----------------------------
# Mention all users individually
# ----------------------------
@app.on_message(
    filters.command(["atag", "amention", "assistanttag", "atagall", "assistag"], prefixes=["/", "@", ".", "#"])
)
async def mention_all_users(_, message):
    # Check if sender is admin
    if not await admins_check(message):
        return await message.reply_text("❌ You must be an admin to use this command.")

    replied = message.reply_to_message

    # Get custom text
    if len(message.command) < 2 and not replied:
        return await message.reply_text(
            "ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴛᴀɢ ᴀʟʟ, ʟɪᴋᴇ » /atag Hi Friends"
        )

    custom_text = message.text.split(None, 1)[1] if not replied else ""

    if message.chat.id in SPAM_CHATS:
        return await message.reply_text("⚠️ Tagging is already running!")

    SPAM_CHATS.append(message.chat.id)

    try:
        async for member in app.get_chat_members(message.chat.id):
            # Stop if cancelled
            if message.chat.id not in SPAM_CHATS:
                break

            # Skip deleted accounts
            if member.user.is_deleted:
                continue

            # Optional: skip bots
            # if member.user.is_bot:
            #     continue

            # Build HTML mention
            first_name = member.user.first_name or "User"
            mention = f'<a href="tg://user?id={member.user.id}">{first_name}</a>'
            text_to_send = f"{custom_text} {mention}" if custom_text else mention

            try:
                if replied:
                    await assistant.send_message(
                        chat_id=replied.chat.id,
                        text=text_to_send,
                        reply_to_message_id=replied.message_id,
                        parse_mode=ParseMode.HTML
                    )
                else:
                    await assistant.send_message(
                        chat_id=message.chat.id,
                        text=text_to_send,
                        parse_mode=ParseMode.HTML
                    )
            except Exception as e:
                print(f"Error mentioning {member.user.id}: {e}")

            # Wait 4 seconds to avoid flooding Telegram
            await asyncio.sleep(4)

        # ✅ Send confirmation after tagging is complete
        await message.reply_text("✅ Tagging complete! All users have been mentioned.")

    finally:
        # Cleanup
        if message.chat.id in SPAM_CHATS:
            SPAM_CHATS.remove(message.chat.id)


# ----------------------------
# Cancel tagging command
# ----------------------------
@app.on_message(
    filters.command(
        [
            "stopmention",
            "offall", 
            "cancel",
            "allstop",
            "stopall",
            "cancelmention",
            "offmention",
            "mentionoff",
            "alloff",
            "cancelall",
            "allcancel",
        ],
        prefixes=["/", "@", "#"],
    )
)
async def cancel_tagging(_, message):
    # Check if sender is admin
    if not await admins_check(message):
        return await message.reply_text("❌ You must be an admin to stop tagging.")

    chat_id = message.chat.id
    if chat_id in SPAM_CHATS:
        SPAM_CHATS.remove(chat_id)
        await message.reply_text("✅ Tagging process successfully stopped!")
    else:
        await message.reply_text("⚠️ No ongoing tagging process!")