"""Python SDK for controlling devices by Evil Genius Labs."""
import asyncio
from typing import Any

from aiohttp import ClientSession


class EvilGeniusDevice:
    """Client class."""

    def __init__(self, host: str, session: ClientSession):
        """Initialize the Evil Genius class."""
        self._session = session
        self.url = f"http://{host}"
        self._request_lock = asyncio.Lock()

    async def get_info(self):
        """Get the info from the Evil Genius service."""
        async with self._request_lock, self._session.get(f"{self.url}/info") as resp:
            return await resp.json()

    async def get_data(self):
        """Get the data from the Evil Genius service."""
        async with self._request_lock, self._session.get(f"{self.url}/all") as resp:
            data = await resp.json()

        return {item["name"]: item for item in data}

    async def set_path_value(self, path: str, value: Any):
        """Sent a value."""
        async with self._request_lock, self._session.post(
            f"{self.url}/{path}?value={value}"
        ) as resp:
            resp.raise_for_status()

    async def set_rgb_color(self, red: int, green: int, blue: int) -> None:
        """Set color."""
        async with self._request_lock, self._session.post(
            f"{self.url}/solidColor?r={red}&g={green}&b={blue}"
        ) as resp:
            resp.raise_for_status()
