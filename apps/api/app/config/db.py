from typing import Any

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from app.enviornment import settings

_client: AsyncIOMotorClient[Any] | None = None


def get_client() -> AsyncIOMotorClient[Any]:

    global _client
    if _client is None:
        _client = AsyncIOMotorClient(settings.MONGO_URL)
    return _client


def close_client() -> None:
    global _client
    if _client is not None:
        _client.close()
        _client = None


def get_database() -> AsyncIOMotorDatabase[Any]:
    return get_client()[settings.MONGO_URL]
