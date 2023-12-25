#(©)Codexbotz
#Recoded By @Its_Tartaglia_Childe

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>┏━━━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━━━┓\n┃ 𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 : <a href='https://t.me/Rokubotz'>𝖱𝗈𝗄𝗎𝖻𝗈𝗍𝗓</a>\n┃ 𝖢𝗋𝖾𝖺𝗍𝗈𝗋 : <a href='tg://user?id={OWNER_ID}'> 𝖶𝖺𝗂𝖿𝗎 </a>\n┃ 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 : <code>𝖯𝗒𝗍𝗁𝗈𝗇3</code>\n┃ 𝖫𝗂𝖻𝗋𝖺𝗋𝗒 : <a href='https://docs.pyrogram.org/'>𝖯𝗒𝗋𝗈𝗀𝗋𝖺𝗆 𝖺𝗌𝗒𝗇𝖼𝗂𝗈 {__version__}</a>\n┃ 𝖲𝗈𝗎𝗋𝖼𝖾 𝖢𝗈𝖽𝖾 : <a href=https://t.me/Salazar5000>𝖳𝖺𝗅𝗄 𝖳𝗈 𝖧𝗂𝗆</a>\n┃ 𝖬𝖺𝗂𝗇 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 : <a href=https://t.me/animesilvervoid>​𝖲𝗂𝗅𝗏𝖾𝗋𝖵𝗈𝗂𝖽</a>\n┃ 𝖲𝗎𝗉𝗉𝗈𝗋𝗍 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 : <a href=https://t.me/Haniflix>𝖧𝖺𝗇𝗂𝖥𝗅𝗂𝗑</a>\n┗━━━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━━━┛</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("𝖢𝗅𝗈𝗌𝖾", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
