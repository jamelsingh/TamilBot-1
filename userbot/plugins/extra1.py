"""Emoji
Available Commands:
.emoji shrug
.emoji apple
.emoji :/
.emoji -_-"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd




@borg.on(admin_cmd(pattern=r"(power*)"))
async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    if input_str == "chod":

        await event.edit(input_str)

        animation_chars = [

            "`என்னைப் பற்றி😏`",
            "`Let's Know About Me 😎`",
            "`பின்னாலிருந்து ஒருவனால் நீ விமர்சிக்கப்பட்டால்,\n\n\nநினைத்துக்கொள்\nநீ அவனை விட ஏதோ ஒன்றில்\n\nமுன்னாடி இருக்கிறாய் என்று..!\n\n 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`பின்னாலிருந்து ஒருவனால் நீ விமர்சிக்கப்பட்டால்,\n\n\nநினைத்துக்கொள்\nநீ அவனை விட ஏதோ ஒன்றில்\n\nமுன்னாடி இருக்கிறாய் என்று..!\n\nவேற ஒன்னு சொல்லட்டுமா?😁... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`பின்னாலிருந்து ஒருவனால் நீ விமர்சிக்கப்பட்டால்,\n\n\nநினைத்துக்கொள்\nநீ அவனை விட ஏதோ ஒன்றில்\n\nமுன்னாடி இருக்கிறாய் என்று..!\n\nவேற ஒன்னு சொல்லட்டுமா?😁... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`பின்னாலிருந்து ஒருவனால் நீ விமர்சிக்கப்பட்டால்,\n\n\nநினைத்துக்கொள்\nநீ அவனை விட ஏதோ ஒன்றில்\n\nமுன்னாடி இருக்கிறாய் என்று..!\n\nவேற ஒன்னு சொல்லட்டுமா?😁... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`பின்னாலிருந்து ஒருவனால் நீ விமர்சிக்கப்பட்டால்,\n\n\nநினைத்துக்கொள்\nநீ அவனை விட ஏதோ ஒன்றில்\n\nமுன்னாடி இருக்கிறாய் என்று..!\n\nவேற ஒன்னு சொல்லட்டுமா?😁... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`பின்னாலிருந்து ஒருவனால் நீ விமர்சிக்கப்பட்டால்,\n\n\nநினைத்துக்கொள்\nநீ அவனை விட ஏதோ ஒன்றில்\n\nமுன்னாடி இருக்கிறாய் என்று..!\n\nவேற ஒன்னு சொல்லட்டுமா?😁... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`பின்னாலிருந்து ஒருவனால் நீ விமர்சிக்கப்பட்டால்,\n\n\nநினைத்துக்கொள்\nநீ அவனை விட ஏதோ ஒன்றில்\n\nமுன்னாடி இருக்கிறாய் என்று..!\n\nவேற ஒன்னு சொல்லட்டுமா?😁... 84%\n█████████████████████▒▒▒▒ `",
            "`பின்னாலிருந்து ஒருவனால் நீ விமர்சிக்கப்பட்டால்,\n\n\nநினைத்துக்கொள்\nநீ அவனை விட ஏதோ ஒன்றில்\n\nமுன்னாடி இருக்கிறாய் என்று..!\n\nவேற ஒன்னு சொல்லட்டுமா?😁... 100%\n█████████████████████████ `",
            "`பின்னாலிருந்து ஒருவனால் நீ விமர்சிக்கப்பட்டால்,\n\n\nநினைத்துக்கொள்\nநீ அவனை விட ஏதோ ஒன்றில்\n\nமுன்னாடி இருக்கிறாய் என்று..!\n\nநாய்-னாகுறைச்சுட்டு தான் இருக்கும். அதற்கெல்லாம் பதில் சொல்லணும்னு அவசியம் இல்லை... 😏 `"
        ]

        animation_interval = 5

        animation_ttl = range(11)

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 10])

@borg.on(admin_cmd(pattern=r"(.*)"))
async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    if input_str == "sqh":

        await event.edit(input_str)

        animation_chars = [

            "`Downloading File..`",
            "`File Downloaded....`",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 84%\n█████████████████████▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 100%\n█████████████████████████ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nTask: 01 of 01 Files Scanned...\n\nResult: No Virus Found...`"
        ]

        animation_interval = 0.1

        animation_ttl = range(11)

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 10])


@borg.on(admin_cmd(pattern=r"(.*)"))
async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    if input_str == "vquickheal":

        await event.edit(input_str)

        animation_chars = [

            "`Downloading File..`",
            "`File Downloaded....`",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 84%\n█████████████████████▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 100%\n█████████████████████████ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nTask: 01 of 01 Files Scanned...\n\nResult:⚠️Virus Found⚠️\nMore Info: Torzan, Spyware, Adware`"
        ]

        animation_interval = 5

        animation_ttl = range(11)

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 10])
