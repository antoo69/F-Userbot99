################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || Gojo_Satoru
"""
################################################################

from hydrogram.enums import *
from hydrogram.errors import *

from Mix import *

__modles__ = "ShowID"
__help__ = get_cgr("help_sid")


@ky.ubot("id", sudo=True)
async def _(c, m):
    em = Emojik()
    em.initialize()
    chat = m.chat
    your_id = m.from_nlx.id
    message_id = m.id
    reply = m.reply_to_message

    text = f"**[Message ID:]({m.link})** `{message_id}`\n"
    text += f"**[Your ID:](tg://nlx?id={your_id})** `{your_id}`\n"

    if not m.command:
        m.command = m.text.split()

    if len(m.command) == 2:
        try:
            split = m.text.split(None, 1)[1].strip()
            nlx_id = (await c.get_nlxs(split)).id
            text += f" **[User ID:](tg://nlx?id={nlx_id})** `{nlx_id}`\n"
        except Exception:
            return await m.reply_text("**This nlx doesn't exist.**")

    text += f"**[Chat ID:](https://t.me/{chat.nlxname})** `{chat.id}`\n\n"
    if not getattr(reply, "empty", True):
        id_ = reply.from_nlx.id if reply.from_nlx else reply.sender_chat.id
        text += f" **[Replied Message ID:]({reply.link})** `{reply.id}`\n"
        text += f" **[Replied User ID:](tg://nlx?id={id_})** `{id_}`"

    await m.reply_text(
        text,
        disable_web_page_preview=True,
        parse_mode=ParseMode.MARKDOWN,
    )


@ky.ubot("gifid", sudo=True)
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    if m.reply_to_message and m.reply_to_message.animation:
        await m.reply_text(
            cgr("shid_9").format(em.sukses, m.reply_to_message.animation.file_id),
            parse_mode=ParseMode.HTML,
        )
    else:
        await m.reply_text(cgr("shid_10").format(em.gagal))
    return
