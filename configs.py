import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", ""))
  API_HASH = os.environ.get("API_HASH", "")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "XB_Filesop_bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002529877348"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "MoneyKamalo.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "0eefb93e1e3ce9470a7033115ceb1bad13a9d674")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "6747520930"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002087398411")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002529877348"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [XB](https://telegram.me/XB_Jitesh) """
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How."""
