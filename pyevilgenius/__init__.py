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
        """Get the info."""
        async with self._request_lock, self._session.get(f"{self.url}/info") as resp:
            return await resp.json()

    async def get_product(self):
        """Get the product name."""
        async with self._request_lock, self._session.get(f"{self.url}/product") as resp:
            return await resp.json()

    async def get_all(self):
        """Get all the data."""
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

    async def get_field_value(self, name: str):
        """Query the field value endpoint."""
        async with self._request_lock, self._session.get(
            f"{self.url}/fieldValue", params={"name": name}
        ) as resp:
            return await resp.text()

    async def set_field_value(self, name: str, value: Any):
        """Set a value using the field value endpoint."""
        async with self._request_lock, self._session.post(
            f"{self.url}/fieldValue", params={"name": name, "value": value}
        ) as resp:
            resp.raise_for_status()
            return await resp.text()
