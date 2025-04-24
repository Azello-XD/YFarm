import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "999"))

DEVS = list(map(int, os.getenv("DEVS", "1927018403").split()))

API_ID = int(os.getenv("API_ID", "27418440"))

API_HASH = os.getenv("API_HASH", "0a08a360e0e9f41b9896f655c300d09d")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7569019566:AAExDhuclLDukfKOZlKv_iNCdb2DOBM9B5A")

OWNER_ID = int(os.getenv("OWNER_ID", "1927018403"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002638098602").split()))

RMBG_API = os.getenv("RMBG_API", "VegrZSZEnnAsufcGsaxECDv6")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://iyaaaaaa:anjingggg@iyaaanjing.uzkxmrz.mongodb.net/?retryWrites=true&w=majority&appName=iyaaanjing")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", " -1002638098602"))
