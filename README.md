# pyevilgenius

## Asynchronous library to control devices by Evil Genius Labs

Requires Python 3.8+ and uses asyncio and aiohttp.

```python
import asyncio
from pprint import pprint

import aiohttp
from pyevilgenius import EvilGeniusDevice


HOST = "192.168.1.113"


async def main():
    async with aiohttp.ClientSession() as session:
        await run(session)


async def run(websession):
    device = pyevilgenius.EvilGeniusDevice(host, websession)
    data = await client.get_data()

    pprint(device.details)

    await device.set_path_value('power', '1')


asyncio.run(main())
```

## Testing locally

```bash
python3 example.py <host>
```

## Timeouts

Pyevilgenius does not specify any timeouts for any requests. You will need to specify them in your own code. We recommend the `async_timeout` package:

```python
import async_timeout

with async_timeout.timeout(10):
    devices = await hub.get_device_list()
```

## Contribution guidelines

Object hierarchy and property/method names should match the Evil Genius Device APIs.
