from datetime import date

from aiogram.filters import BaseFilter
from aiogram.types import Message
from aiogram.filters import CommandObject

from src.database import query_to_db_doctor
from src.database import query_to_db_client


class Is_client(BaseFilter):
    def __init__(self) -> None:
        pass

    async def __call__(self, msg: Message, command: CommandObject):
        try:
            client_id = int(command.args)
            return await query_to_db_client.in_db(client_id=client_id)
        except Exception as e:
            return False


class Valid_full_name(BaseFilter):
    def __init__(self) -> None:
        pass

    async def __call__(self, msg: Message) -> bool:
        try:
            alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
            data = msg.text.lower()
            if len(data.split()) != 3:
                return False
            data = ''.join(data.split())
            return all(c in alphabet for c in data)
        except Exception as e:
            return False


class Valid_age(BaseFilter):
    def __init__(self) -> None:
        pass

    async def __call__(self, msg: Message) -> bool:
        try:
            data = msg.text.split()
            if len(data) != 3:
                return False
            year, month, day = map(int, data)
            date_diff = date.today() - date(year=year, month=month, day=day)
            date_diff = date_diff.days / 365.2425
            return 0 <= date_diff <= 100
        except Exception as e:
            return False


class Is_doctor(BaseFilter):
    def __init__(self) -> None:
        pass

    async def __call__(self, msg: Message) -> bool:
        try:
            return await query_to_db_doctor.is_doctor(telegram_id_doctor=msg.from_user.id)
        except Exception as e:
            return False


class Valid_date(BaseFilter):
    def __init__(self) -> None:
        pass

    async def __call__(self, msg: Message) -> bool:
        try:
            data = msg.text.split()
            if len(data) != 3:
                return False
            year, month, day = map(int, data)
            date(year=year, month=month, day=day)
            return True
        except Exception as e:
            return False


class Valid_date_command(BaseFilter):
    def __init__(self) -> None:
        pass

    async def __call__(self, msg: Message, command: CommandObject) -> bool:
        try:
            data = command.args.split()
            if len(data) != 3:
                return False
            year, month, day = map(int, data)
            date(year=year, month=month, day=day)
            return True
        except Exception as e:
            return False
