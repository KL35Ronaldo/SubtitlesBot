from uuid import uuid4
from pyrogram.types import (
    InlineQuery,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    InlineQueryResultDocument
)
from subtitle import get_lang
from pyrogram import Client as Bot

@Bot.on_callback_query()
async def callback(c: Bot, q: CallbackQuery):
    m = q.message
    index, lang, link = get_lang(q.data.strip().lower())
    if len(index) == 0:
        await m.edit("Something went wrong!")
        return
    btns = [[InlineKeyboardButton(lang[i-1].title(), switch_inline_query_current_chat=link[i-1])] for i in range(len(index))]
    await m.edit(
        text = "Select your language",
        reply_markup = InlineKeyboardMarkup(btns)
    )

@Bot.on_inline_query()
async def inline(c: Bot, q: InlineQuery):
    results = [
        InlineQueryResultDocument(
            document_url=q.query,
            title="Get the File",
            id=uuid4(),
            caption="©️ @GetSubtitles_bot\n\nUse @UnzipTGBot for unzipping this zip file or download the file and unzip manually"
        )
    ]
    await q.answer(results)
