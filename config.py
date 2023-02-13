import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "7782147"))
API_HASH = getenv("API_HASH", "807b64fbb57797086097d274df3a934c")

BOT_TOKEN = getenv("BOT_TOKEN", "5806315236:AAEsKAxRFnLuNRPfeC-wT4bFwJ68J2uV7Zo")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Aman:Aman@cluster0.gt2bc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001811125658"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "ιηƒℓє¢тιση")

OWNER_ID = list(map(int, getenv("OWNER_ID", "1820525265").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AnonymousX1025/AnonXMusic")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/KRISTY_MF")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/KRISTY_AF")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "1800000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "1800000"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "60")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "f4c4aea1021549dbaf6b252d792473c9")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "98afbf53886b413299758e98665e4293")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQChKlbT2MwrusdmlnilHbrdvOwu22Evh0OKHH3Qdn6uteoplXVfpzi-gOeacB8f2RoG_9HUUvyUqBorRzAzx6fWK-ZIXCgji_7mA_oQhu2_8cxe8b8o9GhOkcbZHtAyUMAb_eLK3nMcEG8ljoCXZVVeJTffvCsB8xVCzIF9Qmqa_41q8CYBt5wrXNdux7u_wd_IopOuM2SJdTNZkdcXfndvDrspFyuGoZwmH0iaYerHy3mlwsHm1y0ctyZG00WE6ZaGuNWHU7cdx7utPO5lSlcpLzb6YjLeYANjnKMJ84GwokJGXjsYbAl0vsGomv8PCcaJ6BaZDVBbQ9VeBbnIZxsdAAAAAUqa5dIA")
STRING2 = getenv("STRING_SESSION2", "")
STRING3 = getenv("STRING_SESSION3", "")
STRING4 = getenv("STRING_SESSION4", "")
STRING5 = getenv("STRING_SESSION5", "")

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/1e99f927ea864e9844e99.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph/file/1e99f927ea864e9844e99.jpg",
)

PLAYLIST_IMG_URL = "https://telegra.ph/file/1e99f927ea864e9844e99.jpg"

GLOBAL_IMG_URL = "https://telegra.ph/file/1e99f927ea864e9844e99.jpg"

STATS_IMG_URL = "https://telegra.ph/file/1e99f927ea864e9844e99.jpg"

TELEGRAM_AUDIO_URL = "https://telegra.ph/file/1e99f927ea864e9844e99.jpg"

TELEGRAM_VIDEO_URL = "https://telegra.ph/file/1e99f927ea864e9844e99.jpg"

STREAM_IMG_URL = "https://telegra.ph/file/1e99f927ea864e9844e99.jpg"

SOUNCLOUD_IMG_URL = "https://telegra.ph/file/1e99f927ea864e9844e99.jpg"

YOUTUBE_IMG_URL = "https://telegra.ph/file/1e99f927ea864e9844e99.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/1e99f927ea864e9844e99.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/1e99f927ea864e9844e99.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/1e99f927ea864e9844e99.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://telegra.ph/file/1e99f927ea864e9844e99.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://telegra.ph/file/1e99f927ea864e9844e99.jpg"
