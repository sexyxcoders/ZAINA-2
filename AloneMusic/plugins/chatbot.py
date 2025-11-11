# chatbot.py — ZAINA-2 AI Chat Module
# 🧠 Adds smart conversation handling + /chatbot toggle support
# -----------------------------------------------

import aiohttp
import asyncio
import random
from datetime import datetime


class ChatBot:
    def __init__(self, assistant_client=None):
        self.assistant_client = assistant_client
        self.session = aiohttp.ClientSession()
        self.chat_enabled = {}  # {chat_id: bool}

    # ─────────────────────────────────────────────
    # Chatbot Toggle (Enable / Disable per chat)
    # ─────────────────────────────────────────────
    def toggle(self, chat_id: int, state: bool):
        """Enable or disable chatbot in a chat"""
        self.chat_enabled[chat_id] = state

    def is_enabled(self, chat_id: int) -> bool:
        """Check if chatbot is enabled for a chat"""
        return self.chat_enabled.get(chat_id, True)  # default: enabled

    # ─────────────────────────────────────────────
    # Message handling
    # ─────────────────────────────────────────────
    async def chat(self, user_id: int, text: str, chat_id: int):
        """Main chatbot logic"""
        try:
            # Custom responses (fun / flirty tone)
            low = text.lower()

            if "zaina" in low:
                responses = [
                    "Hey there 💋, I heard my name — what’s up?",
                    "Zaina’s always listening... 😘",
                    "You called me? I’m right here, handsome 💞",
                ]
                return random.choice(responses)

            if any(x in low for x in ["love", "miss", "kiss", "cute"]):
                responses = [
                    "Aww 😳 you’re making me blush!",
                    "That’s so sweet of you 💞",
                    "Hehe… stop it, you’ll make me fall for you 🥰",
                ]
                return random.choice(responses)

            if any(x in low for x in ["hi", "hello", "hey", "yo"]):
                responses = [
                    "Hey cutie 👋",
                    "Hello there ❤️",
                    "Heyy! How’s it going?",
                ]
                return random.choice(responses)

            # API fallback (AI chat)
            async with self.session.get(
                "https://api.classy0.workers.dev",
                params={"message": text, "user": user_id},
                timeout=15,
            ) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data.get("reply", None)
                return None

        except Exception as e:
            print(f"[ChatBot Error] {e}")
            return None

    # ─────────────────────────────────────────────
    # Sticker reaction
    # ─────────────────────────────────────────────
    async def react_to_sticker(self, chat_id: int):
        """React to sticker messages"""
        try:
            if self.assistant_client:
                await self.assistant_client.send_chat_action(chat_id, "choose_sticker")
                await asyncio.sleep(0.5)
                sticker_ids = [
                    "CAACAgUAAxkBAAEHqW1mQb6kXxG8h...",  # Add real sticker IDs
                    "CAACAgUAAxkBAAEHqW9mQb6x3Ux6g...",
                    "CAACAgUAAxkBAAEHqXFmQb7OoR8jF...",
                ]
                await self.assistant_client.send_sticker(chat_id, random.choice(sticker_ids))
        except Exception as e:
            print(f"[ChatBot Sticker Error] {e}")

    # ─────────────────────────────────────────────
    # Cleanup
    # ─────────────────────────────────────────────
    async def close(self):
        await self.session.close()