import datetime

from sqlalchemy import select, insert

from src.database.models.relationship_doctor_of_client import \
    Relationship_doctor_of_client as Relationship_doctor_of_client_model
from src.database.models.doctor import Doctor as Doctor_model

from src.database.models import async_session_factory


class Doctor:

    @staticmethod
    async def add(telegram_id_doctor: int):
        async with async_session_factory() as session:
            query = insert(Doctor_model).values({
                'telegram_id_doctor': telegram_id_doctor,
            })
            await session.execute(query)
            await session.commit()

    @staticmethod
    async def is_doctor(telegram_id_doctor: int) -> bool:
        async with async_session_factory() as session:
            query = select(Doctor_model).filter_by(telegram_id_doctor=telegram_id_doctor)
            result = await session.execute(query)
            result = result.scalars().all()
        return bool(result)

    @staticmethod
    async def create_visit(id_client: int, telegram_id_doctor: int):
        async with async_session_factory() as session:
            query = insert(Relationship_doctor_of_client_model).values({
                'id_client': id_client,
                'telegram_id_doctor': telegram_id_doctor,
                'date_of_visit': datetime.date.today()
            })
            await session.execute(query)
            await session.commit()

    @staticmethod
    async def show_today(telegram_id_doctor: int) -> list[Relationship_doctor_of_client_model]:
        return await Doctor.show_day(telegram_id_doctor=telegram_id_doctor, date=datetime.date.today())

    @staticmethod
    async def show_day(telegram_id_doctor: int, date: datetime.date) -> list[Relationship_doctor_of_client_model]:
        async with async_session_factory() as session:
            query = select(Relationship_doctor_of_client_model).filter_by(telegram_id_doctor=telegram_id_doctor,
                                                                          date_of_visit=date)
            result = await session.execute(query)
            result = result.scalars().all()
        return result
