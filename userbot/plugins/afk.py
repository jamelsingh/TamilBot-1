# Afk plugin from TamilUserBot ported from uniborg
import asyncio
from datetime import datetime

from telethon import events
from telethon.tl import functions, types
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd
from userbot import BOTLOG, BOTLOG_CHATID

global USERAFK_ON
global afk_time
global last_afk_message
global afk_start
global afk_end
USERAFK_ON = {}
afk_time = None
last_afk_message = {}
afk_start = {}


@borg.on(events.NewMessage(outgoing=True))
async def set_not_afk(event):
    if event.chat_id in Config.UB_BLACK_LIST_CHAT:
        return
    global USERAFK_ON
    global afk_time
    global last_afk_message
    global afk_start
    global afk_end
    back_alive = datetime.now()
    afk_end = back_alive.replace(microsecond=0)
    if afk_start != {}:
        total_afk_time = str((afk_end - afk_start))
    current_message = event.message.message
    if "afk" not in current_message and "on" in USERAFK_ON:
        shite = await borg.send_message(
            event.chat_id,
            "__நான் வந்துட்டேன்!... 🥳__\n**இனி இங்குதான்.**\n `நான் Offline-ல் இருந்த நேரம் :``"
            + total_afk_time
            + "`",
        )
        if BOTLOG:
            await borg.send_message(
                BOTLOG_CHATID,
                "#AFKFALSE \nSet AFK mode to False\n"
                + "__நான் வந்துட்டேன்!... 🥳__\n**இனி இங்குதான்.**\n `நான் Offline-ல் இருந்த நேரம் :``"
                + total_afk_time
                + "`",
            )
        await asyncio.sleep(5)
        await shite.delete()
        USERAFK_ON = {}
        afk_time = None


@borg.on(
    events.NewMessage(incoming=True, func=lambda e: bool(e.mentioned or e.is_private))
)
async def on_afk(event):
    if event.fwd_from:
        return
    global USERAFK_ON
    global afk_time
    global last_afk_message
    global afk_start
    global afk_end
    back_alivee = datetime.now()
    afk_end = back_alivee.replace(microsecond=0)
    if afk_start != {}:
        total_afk_time = str((afk_end - afk_start))
    current_message_text = event.message.message.lower()
    if "afk" in current_message_text:
        # userbot's should not reply to other userbot's
        # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
        return False
    if USERAFK_ON and not (await event.get_sender()).bot:
        msg = None
        message_to_reply = (
            f"__நான் Offline சென்று__ `{total_afk_time}`ஆகிறது😝.\nஎன்ன கொஞ்ச நேரம் நிம்மதியாக விடுங்க... 🚶‍♂🚶‍♂🚶‍♂ "
            + f"\n\n__நான் திரும்பி வந்ததும் உங்களுக்கு பதிலளிக்கிறேன் 😊__\n**நான் Offline செல்ல காரணம்**: {reason}"
            if reason
            else f"**வனக்கம்!**\n__நான் Offline-ல் உள்ளேன். எப்போது, நீங்கள் கேட்க? {total_afk_time} -க்கு நான் நினைக்கிறேன்.__\n\nநான் எப்போது திரும்பி வருவேன்? விரைவில் __நான் அதை உணரும்போதெல்லாம்__**( ಠ ʖ̯ ಠ)**  "
        )
        if event.chat_id not in Config.UB_BLACK_LIST_CHAT:
            msg = await event.reply(message_to_reply)
        if event.chat_id in last_afk_message:
            await last_afk_message[event.chat_id].delete()
        last_afk_message[event.chat_id] = msg
        await asyncio.sleep(5)
        hmm = await event.get_chat()
        if Config.PM_LOGGR_BOT_API_ID:
            await asyncio.sleep(5)
            if not event.is_private:
                await event.client.send_message(
                    Config.PM_LOGGR_BOT_API_ID,
                    f"#AFK_TAGS \n<b>Group : </b><code>{hmm.title}</code>\
                            \n<b>Message : </b><a href = 'https://t.me/c/{hmm.id}/{event.message.id}'> link</a>",
                    parse_mode="html",
                    link_preview=False,
                )


@borg.on(admin_cmd(pattern=r"afk ?(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    global USERAFK_ON
    global afk_time
    global last_afk_message
    global afk_start
    global afk_end
    global reason
    USERAFK_ON = {}
    afk_time = None
    last_afk_message = {}
    afk_end = {}
    if not USERAFK_ON:
        start_1 = datetime.now()
        afk_start = start_1.replace(microsecond=0)
        reason = event.pattern_match.group(1)
        last_seen_status = await borg(
            functions.account.GetPrivacyRequest(types.InputPrivacyKeyStatusTimestamp())
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            afk_time = datetime.now()
        USERAFK_ON = f"on: {reason}"
        if reason:
            await borg.send_message(
                event.chat_id, f"**நான் Offline செல்கிறேன்!** __ஏனெனில்,  {reason}__"
            )
        else:
            await borg.send_message(event.chat_id, '**நான் Offline செல்கிறேன்!**')
        await asyncio.sleep(5)
        await event.delete()
        if BOTLOG:
            await borg.send_message(
                BOTLOG_CHATID,
                f"#AFKTRUE \nSet AFK mode to True, and Reason is {reason}",
            )
