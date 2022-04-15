import asyncio
import sys
import logging

import aiohttp

import pyevilgenius


async def main():
    logging.basicConfig(level=logging.DEBUG)
    async with aiohttp.ClientSession() as session:
        await run(session)


async def run(websession):
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <host>")
        return

    host = sys.argv[1]
    device = pyevilgenius.EvilGeniusDevice(host, websession)

    data = await device.get_all()

    for item in data.values():
        if "value" not in item:
            continue
        value = item["value"]
        if "options" in item:
            value = item["options"][value]
        print(f"{item['label']}: {value}")


try:
    asyncio.run(main())
except KeyboardInterrupt:
    pass
