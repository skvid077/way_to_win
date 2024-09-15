import asyncio

from src.database.models.base import async_engine, async_session_factory, Base
from src.database.models.relationship_doctor_of_client import Relationship_doctor_of_client
from src.database.models.doctor import Doctor
from src.database.models.client import Client


async def reload_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


if __name__ == '__main__':
    asyncio.run(reload_db())
