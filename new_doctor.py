import asyncio
from src.database import query_to_db_doctor


async def main():
    try:
        f = open(file='new_doctor.txt', mode='r')
        id_new_doctor = int(f.readline())
        await query_to_db_doctor.add(telegram_id_doctor=id_new_doctor)
        f.close()
    except Exception as e:
        print('error')
        print(e)


asyncio.run(main())
