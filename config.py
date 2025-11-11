#
# Copyright (C) 2021-2022 by TheAloneteam@Github, < https://github.com/TheAloneTeam >.
#
# This file is part of < https://github.com/TheAloneTeam/TheAloneMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TheAloneTeam/TheAloneMusic/blob/master/LICENSE >
# All rights reserved.

import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "22657083"))
API_HASH = getenv("API_HASH", "d6186691704bd901bdab275ceaab88f3")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "8278474473:AAEo5e_-bf0q1uSCkFYSvpdd3GW40SybhT0")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://pikachuxivan_db_user:pikachuxivan@cluster0.9c3hko7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

# Set this to true if you want post ads automatically
ADS_MODE = getenv("ADS_MODE", None)

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", " -1003253055582"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "8449801101"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/sexyxcoders/ZAINA-2",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TncNetwork")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TNCmeetups")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", None))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQCOaU4ADKvT2BTxQXSza_DvPCOW1NyGilYWq7JuIv8rwVhXwUL1puCJBK17KcAScIOeDTPY8PgXMwUyLPJ_bKHNrSfHT8eFK5xmgshRrWS86ZAav1opc1k9DqxyojhBVVijw9yK584qewDTsq2RR85grokWj2L7egpA0pV4MLMIrYTTSecxnSvuBID7KojBPd1YhcFe8rK35HINpDsW0_KpS3GTrg3pkHpP1uVdUdtf6jjTdYzNAz1_929lNPZtDYZTFzzfbXHE1Ylx0s4-7TGk9zSPB0Qahzd3Zzu2WiwpjfZFnIUc6qiHVxxiYQWd1jTFTGxtov5GIAEOlXGTfW3anDH_RQAAAAHwwIkLAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL",
    "https://graph.org/file/004b61545b493662eacf1-71a5b2f2f11ff4a41a.jpg",
)
PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://graph.org/file/004b61545b493662eacf1-71a5b2f2f11ff4a41a.jpg",
)
PLAYLIST_IMG_URL = "https://graph.org/file/004b61545b493662eacf1-71a5b2f2f11ff4a41a.jpg"
STATS_IMG_URL = "https://graph.org/file/004b61545b493662eacf1-71a5b2f2f11ff4a41a.jpg"
TELEGRAM_AUDIO_URL = (
    "https://graph.org/file/004b61545b493662eacf1-71a5b2f2f11ff4a41a.jpg"
)
TELEGRAM_VIDEO_URL = (
    "https://graph.org/file/004b61545b493662eacf1-71a5b2f2f11ff4a41a.jpg"
)
STREAM_IMG_URL = "https://graph.org/file/004b61545b493662eacf1-71a5b2f2f11ff4a41a.jpg"
SOUNCLOUD_IMG_URL = (
    "https://graph.org/file/004b61545b493662eacf1-71a5b2f2f11ff4a41a.jpg"
)
YOUTUBE_IMG_URL = "https://graph.org/file/004b61545b493662eacf1-71a5b2f2f11ff4a41a.jpg"
SPOTIFY_ARTIST_IMG_URL = (
    "https://graph.org/file/004b61545b493662eacf1-71a5b2f2f11ff4a41a.jpg"
)
SPOTIFY_ALBUM_IMG_URL = (
    "https://graph.org/file/004b61545b493662eacf1-71a5b2f2f11ff4a41a.jpg"
)
SPOTIFY_PLAYLIST_IMG_URL = (
    "https://graph.org/file/004b61545b493662eacf1-71a5b2f2f11ff4a41a.jpg"
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
