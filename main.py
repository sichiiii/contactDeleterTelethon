import re
import asyncio

from telethon import functions, utils
from telethon.sync import TelegramClient

name = 'deleter'
api_id = ###
api_hash = ###

async def main():
    async with TelegramClient(name, api_id, api_hash) as client:
        result = await client(functions.contacts.GetContactsRequest(hash=0))

        for u in result.users:
            match = re.search('\d \d', utils.get_display_name(u))

            if match:
                result = await client(functions.contacts.DeleteContactsRequest(
                    id=[u]
                ))
                print(result.stringify())
            else:
                pass

asyncio.run(main())
