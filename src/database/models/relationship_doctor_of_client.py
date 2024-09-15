import datetime

from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base


class Relationship_doctor_of_client(Base):
    __tablename__ = 'relationship_doctor_of_client'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)
    id_client: Mapped[int] = mapped_column(primary_key=False)
    telegram_id_doctor: Mapped[int] = mapped_column(primary_key=False)
    date_of_visit: Mapped[datetime.date] = mapped_column(nullable=False)
