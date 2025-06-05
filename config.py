# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "26330942"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "5de9fd033aa828dfd3bf0c28adeee660")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7363509425:AAF92zS7bv50rpuH6NtlaCN-BOf1GmTaMAM")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("@Sujalbbbot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "6883471516"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6883471516").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002618428217"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://biklriplit:efaXfv2Ps9MRfner@cluster0.4hfu8zj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", ""))

