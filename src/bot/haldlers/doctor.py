from aiogram import Bot, Dispatcher, types, Bot, F
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.state import State
from src.bot.commands import doctor as command_doctor
from src.bot.filters import doctor as filters_doctor
from src.bot.states import doctor as states_doctor


async def register(dp: Dispatcher):
    dp.message.register(command_doctor.id_,
                        Command('id')
                        )
    dp.message.register(command_doctor.start,
                        CommandStart(),
                        filters_doctor.Is_doctor()
                        )
    dp.message.register(command_doctor.cancel,
                        Command('cancel'),
                        State('*'),
                        filters_doctor.Is_doctor()
                        )
    dp.message.register(command_doctor.add_user,
                        Command('add_user'),
                        State('*'),
                        filters_doctor.Is_doctor()
                        )
    dp.message.register(command_doctor.get_full_name,
                        StateFilter(states_doctor.Add_client.full_name),
                        filters_doctor.Is_doctor(),
                        filters_doctor.Valid_full_name(),
                        F.text
                        )
    dp.message.register(command_doctor.get_full_name_error,
                        StateFilter(states_doctor.Add_client.full_name),
                        filters_doctor.Is_doctor()
                        )
    dp.message.register(command_doctor.get_age,
                        StateFilter(states_doctor.Add_client.age),
                        filters_doctor.Is_doctor(),
                        filters_doctor.Valid_age(),
                        filters_doctor.Valid_date(),
                        F.text
                        )
    dp.message.register(command_doctor.get_age_error,
                        StateFilter(states_doctor.Add_client.age),
                        filters_doctor.Is_doctor(),
                        filters_doctor.Valid_date(),
                        F.text
                        )
    dp.message.register(command_doctor.get_date_error,
                        StateFilter(states_doctor.Add_client.age),
                        filters_doctor.Is_doctor()
                        )
    dp.message.register(command_doctor.add_admission,
                        Command('add_admission'),
                        filters_doctor.Is_doctor(),
                        filters_doctor.Is_client(),
                        )
    dp.message.register(command_doctor.add_admission_error,
                        Command('add_admission'),
                        filters_doctor.Is_doctor()
                        )
    dp.message.register(command_doctor.get_clients_today,
                        Command('get_client_today'),
                        filters_doctor.Is_doctor()
                        )
    dp.message.register(command_doctor.get_clients_day,
                        Command('get_client_day'),
                        filters_doctor.Is_doctor(),
                        filters_doctor.Valid_date_command()
                        )
    dp.message.register(command_doctor.get_date_error,
                        Command('get_client_day'),
                        filters_doctor.Is_doctor(),
                        )


async def command_register(bot: Bot):
    await bot.set_my_commands([
        types.BotCommand(command="start",
                         description="Старт бота"),
        types.BotCommand(command='cancel',
                         description='Удаление состояния'),
        types.BotCommand(command='id',
                         description='Ваш ID'),
        types.BotCommand(command='add_user',
                         description='Добавить пользователя по шагам 1) ФИО 2) Год рождения(YYYY MM DD)'),
        types.BotCommand(command='add_admission',
                         description='Добавить приём пользователя /add_admission __ID пользователя__'),
        types.BotCommand(command='get_client_today',
                         description='Получить количество посещений сегодня'),
        types.BotCommand(command='get_client_day',
                         description='Получить количество посещений в любой день')
    ])
