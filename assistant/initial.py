# AnekaShastraHasta - UserBot
# Copyright (C) 2021-2022 TeamAnekaShastraHasta
#
# This file is a part of < https://github.com/TeamAnekaShastraHasta/AnekaShastraHasta/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamAnekaShastraHasta/AnekaShastraHasta/blob/main/LICENSE/>.

import re

from . import *

STRINGS = {
    1: """🎇 **Thanks for Deploying AnekaShastraHasta Userbot!**

• Here, are the Some Basic stuff from, where you can Know, about its Usage.""",
    2: """🎉** About AnekaShastraHasta**

🧿 AnekaShastraHasta is Pluggable and powerful Telethon Userbot, made in Python from Scratch. It is Aimed to Increase Security along with Addition of Other Useful Features.

❣ Made by **@TeamAnekaShastraHasta**""",
    3: """**💡• FAQs •**

-> [Username Tracker](https://t.me/AnekaShastraHastaUpdates/24)
-> [Keeping Custom Addons Repo](https://t.me/AnekaShastraHastaUpdates/28)
-> [Disabling Deploy message](https://t.me/AnekaShastraHastaUpdates/27)
-> [Setting up TimeZone](https://t.me/AnekaShastraHastaUpdates/22)
-> [About Inline PmPermit](https://t.me/AnekaShastraHastaUpdates/21)
-> [About Dual Mode](https://t.me/AnekaShastraHastaUpdates/18)
-> [Custom Thumbnail](https://t.me/AnekaShastraHastaUpdates/13)
-> [About FullSudo](https://t.me/AnekaShastraHastaUpdates/11)
-> [Setting Up PmBot](https://t.me/AnekaShastraHastaUpdates/2)
-> [Also Check](https://t.me/AnekaShastraHastaUpdates/14)

**• To Know About Updates**
  - Join @TeamAnekaShastraHasta.""",
    4: f"""• `To Know All Available Commands`

  - `{HNDLR}help`
  - `{HNDLR}cmds`""",
    5: """• **For Any Other Query or Suggestion**
  - Move to **@AnekaShastraHastaSupportChat**.

• Thanks for Reaching till END.""",
}


@callback(re.compile("initft_(\\d+)"))
async def init_depl(e):
    CURRENT = int(e.data_match.group(1))
    if CURRENT == 5:
        return await e.edit(
            STRINGS[5],
            buttons=Button.inline("<< Back", "initbk_4"),
            link_preview=False,
        )

    await e.edit(
        STRINGS[CURRENT],
        buttons=[
            Button.inline("<<", f"initbk_{str(CURRENT - 1)}"),
            Button.inline(">>", f"initft_{str(CURRENT + 1)}"),
        ],
        link_preview=False,
    )


@callback(re.compile("initbk_(\\d+)"))
async def ineiq(e):
    CURRENT = int(e.data_match.group(1))
    if CURRENT == 1:
        return await e.edit(
            STRINGS[1],
            buttons=Button.inline("Start Back >>", "initft_2"),
            link_preview=False,
        )

    await e.edit(
        STRINGS[CURRENT],
        buttons=[
            Button.inline("<<", f"initbk_{str(CURRENT - 1)}"),
            Button.inline(">>", f"initft_{str(CURRENT + 1)}"),
        ],
        link_preview=False,
    )
