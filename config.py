import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

COMMAND_PREFIX = [",", ".", "/", "!"]

DEVELOPER_ID = int(os.getenv("DEVELOPER_ID"))
UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL")

ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS").split()))

MONGO_URL = os.getenv("MONGO_URL")
