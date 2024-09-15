import datetime

from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base, str_50


class Client(Base):
    __tablename__ = 'client'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)
    name: Mapped[str_50] = mapped_column(nullable=False)
    age: Mapped[datetime.date] = mapped_column(nullable=False)
