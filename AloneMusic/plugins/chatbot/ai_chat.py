
# ai_chat.py — ChatBot Plugin for ZAINA-2 Music Bot
# 🔥 Adds /chatbot toggle + auto AI reply for text & sticker
# ---------------------------------------------------------

import asyncio
from pyrogram import filters
from pyrogram.types import Message
from AloneMusic import app
from chatbot import ChatBot

chat_ai = ChatBot(app)


# ─────────────────────────────────────────────
# 🔘 Command: /chatbot enable | disable
# ─────────────────────────────────────────────
@app.on_message(filters.command(["chatbot"]) & filters.group)
async def chatbot_toggle(_, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Usage: `/chatbot enable` or `/chatbot disable`", quote=True)

    cmd = message.command[1].lower()
    chat_id = message.chat.id

    if cmd == "enable":
        chat_ai.toggle(chat_id, True)
        await message.reply_text("🤖 **Chatbot enabled** for this group.")
    elif cmd == "disable":
        chat_ai.toggle(chat_id, False)
        await message.reply_text("🚫 **Chatbot disabled** for this group.")
    else:
        await message.reply_text("Invalid option! Use `enable` or `disable` only.")


# ─────────────────────────────────────────────
# 💬 Auto reply to messages
# ─────────────────────────────────────────────
@app.on_message(filters.text & ~filters.command(["chatbot"]))
async def chatbot_reply(_, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else 0
    text = message.text

    if not chat_ai.is_enabled(chat_id):
        return  # chatbot disabled in this chat

    # Ignore commands, bots, etc.
    if message.from_user and message.from_user.is_bot:
        return

    # Typing action
    await app.send_chat_action(chat_id, "typing")

    # Generate response
    response = await chat_ai.chat(user_id, text, chat_id)
    if response:
        await asyncio.sleep(1.5)
        await message.reply_text(response)


# ─────────────────────────────────────────────
# 🧸 Sticker reactions
# ─────────────────────────────────────────────
@app.on_message(filters.sticker & filters.group)
async def chatbot_sticker(_, message: Message):
    chat_id = message.chat.id
    if not chat_ai.is_enabled(chat_id):
        return
    await chat_ai.react_to_sticker(chat_id)


# ─────────────────────────────────────────────
# 🧹 Cleanup when bot stops
# ─────────────────────────────────────────────
@app.on_message(filters.command("shutdown"))
async def shutdown(_, message: Message):
    await chat_ai.close()
    await message.reply_text("🧠 Chat session closed. Bye-bye!")