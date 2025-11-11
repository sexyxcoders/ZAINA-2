from pyrogram import Client
import config

# Initialize the assistant client using STRING1 (or STRING2/3…)
assistant = Client(
    "assistant",
    session_string=config.STRING1  # Must be set in your config.py
)