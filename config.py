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

STRING1 = getenv("STRING_SESSION", "BQB87TW3f0Vefbu2zIXDIoixeOExUoTyK6ESmR9BZvVTS3ssLbKF0n3pUfQAaz3hMYJchiuQmQM1Cebm6RwaNsuIW47Oedx7BnI8QudZCN_PRCh4XkJUTRI6raz65hov3BBY9-prWolordDHtfuRru6TZ3fZNx8amr3zwPOkkc8HnxHD4MOgYRWfcWdC3_xO2KDPHPrmkW0hFV9Ttq7h_mDrlKePJZheGIBjCAIEfdfT3rvjGfq9v5aO78iSRysxTzYqSXQuEgGvGSrw8osWelLzQT9r0hATv8vwlGMIEtOFm-2ok19Iaj2x2Oup3It--PKlwjnpxk8lcpQV8nwbV_8uAAAAAW_jzX8A")
STRING2 = getenv("STRING_SESSION2", "BQBm_uqtUhVIjBkKp6Ai_BJ7lpvDgY5QpidpsXgj4QsNkZi5UiP3zv9GQqsRxBU6CPBunfbNlemN9uBZo2KTC6r325kIoUJeuPtJ40F_EAAh5wai1Twl1kfAMPE7hNjkhrNfCx6PgHdyadzfZX0VxSajoVP3LMxaYqBZID-3CiX68XjmiOXZ4EB7a0IVsqgxoskzGfYPFtSn1H4rB6ZHi_W5oqh0sJ3iAy7xA86VsTvgK8xZSC5pci9LbAgfZQ48YN3XFzGQgiZXNtv1v-fbCsloGzO8wneXQz3NtPd05IHnI0kqhrn2mLVOWP9vspbJbu_2K-M_Z-mBKbuL8Qt2ZhqhAAAAAVpdYS8A")
STRING3 = getenv("STRING_SESSION3", "BQBdy48LSbN667RvtxEiJZL0CbRqkyzFxz-Z-juGnyizfrtjkOWzQI28dwaCBNxGxy6A91NpmQGUHRF6Fa96-Lhd23VCzqui6nxSfrW5py5ojrGvfyQd8wQkIbF0f9D26VbldxKqcA4rnbfyj45QCKBoiW7gN4N1xlEXwpxZLNC74v1vn11wb2wVY7oaYfEGoxgBZuhlL1j1zIiJ7TZrjKMoyE62Z0SbdRRgj07KFHRZqUo_5XyXLyOaRY_zsyRaTcxqDbUVZVz3FsosWmNSSKoNHZPUHT3Sox66ka6nlMqXkvXMzK9c0AsW4VvnZ525RQ81Hc7aw8M-qyJNngQRh6lEAAAAAXDhFr4A")
STRING4 = getenv("STRING_SESSION4", "BQAxnLXutpLXPscQ0GJ_j3QQ6diOBQPO_2o0YFXLidJd4XX8nlgGoCcNNUuWVKgy423p8zWZXOpp-cseSodbtSSj-Tc4hq5t2JzqzZzwq0HLESQ7A5o4do86UuWaGTijT9H652X1iPSxVK_-YRLuc5g7dzx2atsfY6fSRD94a44rRXq84ibkO_12kfBGjeIdXj6qjIXzcQYGdMIea0r65EIMIq_G6AEORpx6ufC5Ki1kfyU6EKfdRojXAYovwmnGGpR2-32fUfMYNOII0UspY65YdIiw0E2gjyUfDlOLEAcDJahyRM6BaEU6y7q8Y2T_1xsyqyfjr-Q2aKAaHN7Jiv9OAAAAAWq35g4A")
STRING5 = getenv("STRING_SESSION5", "BQCeX1JH4vkV8sXZIkh8vvonQIeTA_p9ssRoXyEsYrc7GsklwQnHZy9Ksgpz7xXEaeiwiZ3neWa4jiL3s3m5eeGWWPhCvNG0IQo9Lw5clcqVKRccP0PuBWhRL3zQaLam_n_8xB7iDcMDaKfh3vmXBH_cvQ4JxnYJ4UbxkZJr5gmyKrdJES3gf_WweXZowAbW61zcruDO26l8A2NAPY4Oy4NSwmofTeT5z4iOhNFdkm36nFL15fd0a2GLqWwdZtKbSvawzhPoTusExsJc5BJnDHpqK-mm8huOO1I8JHf4CCgh0eDMcwSaAun0dJ908jxV6yUOkbneuF4NbRv2s5GMxJdHAAAAAW69v4YA")

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
