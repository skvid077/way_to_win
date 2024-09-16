import datetime

from sqlalchemy import select, insert

from src.database.models.client import Client as Client_model

from src.database.models import async_session_factory


class Client:

    @staticmethod
    async def in_db(client_id: int) -> bool:
        async with async_session_factory() as session:
            query = select(Client_model).filter_by(id=client_id)
            result = await session.execute(query)
            result = result.scalars().all()
        return bool(result)

    @staticmethod
    async def add(name: str, age: datetime.datetime):
        async with async_session_factory() as session:
            query = insert(Client_model).values({
                'name': name,
                'age': age
            })
            await session.execute(query)
            await session.commit()
