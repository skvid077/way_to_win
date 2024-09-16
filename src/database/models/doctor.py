from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base


class Doctor(Base):
    __tablename__ = 'doctor'
    telegram_id_doctor: Mapped[int] = mapped_column(primary_key=True, autoincrement=False, unique=True)
