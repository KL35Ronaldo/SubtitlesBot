from subtitles import search_sub
from pyrogram import Client as Bot, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Bot.on_message(filters.command('start'))
async def start(c: Bot, m: Message):
    await m.reply(f"Hi *{m.from_user.first_name}*!\n\nI am subtitle downloader bot. I can provide movie subtitles.\n\n==> Just send me Movie name. Use @imdb inline to get correct movie name.")

@Bot.on_message(filters.text)
async def searching(c: Bot, m: Message):
    msg = await m.reply("Searching your subtitle file")
    all, title, key = await search_sub(m.text.strip().lower())
    if len(all) == 0:
        await msg.edit("No results found")
        return
    btns = [[InlineKeyboardButton(title[i-1], key[i-1])] for i in all[:15]]
    await msg.edit(
        text = f"Got the following results for your query *{m.text.strip().lower()}*. Select the preffered type from the below options",
        reply_markup = InlineKeyboardMarkup(btns)
    )
