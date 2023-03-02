import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "24699892"))
API_HASH = getenv("API_HASH", "7677c107cfce8ca298c61fe29e07c874")

BOT_TOKEN = getenv("BOT_TOKEN", "6231987832:AAGjLfNj83LBka3LNjAh1eiCPdeiPLL3NEU")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Aman:Aman@cluster0.gt2bc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001639873014"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "𓆩᪵🅵𝟐🅵𓆪 ✘ 𝙈𝙐𝙎𝙄𝘾 🇮🇳")

OWNER_ID = list(map(int, getenv("OWNER_ID", "2017352340").split()))

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

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQAKpAoRWVH_GWkQyxLNKpiF4TJdBz_RzR05Wlb9La93gNZWoKtgVmJlhXXQB2OZie90upQrKUj9xZ0hy7NBF56XfUY2J7l_Rh2epM5iobKkTmja-NZvjIE3v4k3M0E9piGT-Sot5EMwEHuhd8zzdHHiMdq1D3AsEgArUegTYzppMKR8On1hyDJU-V9VKrxVBCtoAgQFjHm8Jlg_eRiPKjQGCPiclc4_JOTj7BxqOcwcKmaVu6OqpnbsIqeRTOfHJ3eF1B5nhJDilojFxJUBzNQD-M1q6vm7JHLgn6yH3O_rodPmfu-iMr1lacZiBNxKLjnHYNnv_r8isk-J1zyJltE5AAAAAUrEEDMA")
STRING2 = getenv("STRING_SESSION2", "BQAiLF2SJSPfgx9ndoW_1ZrDVYqZCFd8wknhqSTZbZEqmxP2UBrobWrSixLJ3hGPjBBPtMzAqTFE355JME92sp9KUfmYyoeoF3bNgJ_0EbOyZse9jqy5N1LbvDO6yJMlaYZdjcdjsPkWJLfXce8gU88vzviX_LmpAf5qYj3E9WH5NXHhDf4BstoU5YOyq0f_ngIwBKB3ZQJKBFvu1YwcgepxROtaRz-chH7bffDX3LW42m2Rrtz0TQGKW2QRYC2EeekF-J00BUP2X08mkcOAMa96-DJoOfl0VEkSMKlvNEIBWOOKzIbmgEcx-QXbGbShY--yztlG-CyQDxDFcRFkzn0CAAAAAT0x1ekA")
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


START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/7fe712e610a78c12769fb.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph/file/7fe712e610a78c12769fb.jpg",
)

PLAYLIST_IMG_URL = "https://telegra.ph/file/7fe712e610a78c12769fb.jpg"

GLOBAL_IMG_URL = "https://telegra.ph/file/7fe712e610a78c12769fb.jpg"

STATS_IMG_URL = "https://telegra.ph/file/7fe712e610a78c12769fb.jpg"

TELEGRAM_AUDIO_URL = "https://telegra.ph/file/7fe712e610a78c12769fb.jpg"

TELEGRAM_VIDEO_URL = "https://telegra.ph/file/7fe712e610a78c12769fb.jpg"

STREAM_IMG_URL = "https://telegra.ph/file/7fe712e610a78c12769fb.jpg"

SOUNCLOUD_IMG_URL = "https://telegra.ph/file/7fe712e610a78c12769fb.jpg"

YOUTUBE_IMG_URL = "https://telegra.ph/file/7fe712e610a78c12769fb.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/7fe712e610a78c12769fb.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/7fe712e610a78c12769fb.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/7fe712e610a78c12769fb.jpg"


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
            PING_IMG_URL = "https://telegra.ph/file/7fe712e610a78c12769fb.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://telegra.ph/file/7fe712e610a78c12769fb.jpg"
