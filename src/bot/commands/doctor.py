from aiogram.types import Message
from aiogram.filters import CommandObject
from aiogram.fsm.context import FSMContext
from src.database import query_to_db_doctor, query_to_db_client
from datetime import date
from src.bot.states.doctor import Add_client as Add_client_state_doctor


async def start(msg: Message):
    await msg.answer(text=f'Здравствуйте, {msg.from_user.first_name}')


async def id_(msg: Message):
    await msg.answer(text=str(msg.from_user.id))


async def cancel(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer(text='Состояние обнулено')


async def add_user(msg: Message, state: FSMContext):
    await state.clear()
    await state.set_state(Add_client_state_doctor.full_name)
    await msg.answer(text='Введите ФИО пациента')


async def add_admission(msg: Message, command: CommandObject):
    await query_to_db_doctor.create_visit(id_client=int(command.args), telegram_id_doctor=msg.from_user.id)
    await msg.answer(text='Приём зафиксирован')


async def add_admission_error(msg: Message):
    await msg.answer(text='Такого пациента не существует')


async def get_full_name(msg: Message, state: FSMContext):
    data = await state.get_data()
    data['full_name'] = msg.text
    await state.set_data(data)
    await state.set_state(Add_client_state_doctor.age)
    await msg.answer(text='Введите дату рождения пациента')


async def get_age(msg: Message, state: FSMContext):
    year, month, day = map(int, msg.text.split())
    date_ = date(year=year, month=month, day=day)
    data = await state.get_data()
    data['age'] = date_
    await query_to_db_client.add(name=data['full_name'], age=data['age'])
    await state.clear()
    await msg.answer(text='Пациент добавлен')


async def get_age_error(msg: Message, state: FSMContext):
    await msg.answer(text='Возраст пациента не может быть больше 100 лет')


async def get_clients_today(msg: Message):
    result = await query_to_db_doctor.show_today(msg.from_user.id)
    await msg.answer(text=f'Сегодня пришло пациентов: {len(result)}')


async def get_clients_day(msg: Message, command: CommandObject):
    year, month, day = map(int, command.args.split())
    date_ = date(year=year, month=month, day=day)
    result = await query_to_db_doctor.show_day(msg.from_user.id, date_)
    await msg.answer(text=f'За {year}.{month}.{day} пришло пациентов: {len(result)}')


async def get_date_error(msg: Message):
    await msg.answer(text=f'Напишите корректную дату вида: YYYY MM DD')


async def get_full_name_error(msg: Message):
    await msg.answer(text='Напишите ФИО тремя отдельными словами без специальных символов')
