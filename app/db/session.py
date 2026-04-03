import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL=os.getenv("DATABASE_URL")

class DataBase:
    pool = None

    @classmethod
    async def connect(cls):
        cls.pool = await asyncpg.create_pool(DATABASE_URL)

    @classmethod
    async def discount(cls):
        await cls.pool.close()

    @classmethod
    async def execute(cls, query : str, *args):
        async with cls.pool.acquire() as conn:
            return await conn.fetch(query, *args)
        
