#(©)CodeXBotz
#Recoded By @Its_Tartaglia_Childe



import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = ("6939464604:AAHPNWfA7QvWt2h12_zM6BgxxAoXtRpULAk")

#Your API ID from my.telegram.org
APP_ID = int("14516437")

#Your API Hash from my.telegram.org
API_HASH = ("8e2d6c40aa1be21b67acd38fe29a07a4")

#Your db channel Id
CHANNEL_ID = int("-1001901878734")

#OWNER ID
OWNER_ID = int("1582227872")

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = ("mongodb+srv://ROKU:ROKU@cluster0.nxjre0s.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "0")

#force sub channel id, if you want enable force sub
FORCESUB_CHANNEL = int("-1001578148295")
FORCESUB_CHANNEL2 = int("-1001816446904")

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "𝐇𝐢 𝐃𝐮𝐝𝐞.. {first}\n\n𝐈 𝐀𝐦 𝐚 𝐅𝐢𝐥𝐞-𝐒𝐭𝐨𝐫𝐞 𝐛𝐨𝐭\n𝐘𝐨𝐮 𝐜𝐚𝐧 𝐚𝐜𝐜𝐞𝐬𝐬 𝐟𝐢𝐥𝐞𝐬 𝐭𝐡𝐫𝐨𝐮𝐠𝐡 𝐚 𝐬𝐩𝐞𝐜𝐢𝐟𝐢𝐜 𝐥𝐢𝐧𝐤..!")
try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "5205293211").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝐒𝐨𝐫𝐫𝐲 𝐒𝐢𝐫/𝐌𝐚𝐦 𝐲𝐨𝐮 𝐡𝐚𝐯𝐞 𝐭𝐨 𝐣𝐨𝐢𝐧 𝐦𝐲 𝐜𝐡𝐚𝐧𝐧𝐞𝐥𝐬 𝐟𝐢𝐫𝐬𝐭 𝐭𝐨 𝐚𝐜𝐜𝐞𝐬𝐬 𝐟𝐢𝐥𝐞𝐬..\n\n𝐒𝐨 𝐩𝐥𝐞𝐚𝐬𝐞 𝐣𝐨𝐢𝐧 𝐦𝐲 𝐜𝐡𝐚𝐧𝐧𝐞𝐥𝐬 𝐟𝐢𝐫𝐬𝐭 𝐚𝐧𝐝 𝐭𝐫𝐲 𝐚𝐠𝐚𝐢𝐧....!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "𝐏𝐥𝐞𝐚𝐬𝐞 𝐝𝐨𝐧𝐭 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐦𝐞 𝐝𝐢𝐫𝐞𝐜𝐭𝐥𝐲 𝐈 𝐜𝐚𝐧𝐭 𝐝𝐨 𝐚𝐧𝐲𝐭𝐡𝐢𝐧𝐠 𝐨𝐭𝐡𝐞𝐫 𝐭𝐡𝐚𝐧 𝐚𝐝𝐦𝐢𝐧𝐬..!"

ADMINS.append(OWNER_ID)
ADMINS.append(6376328008)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
