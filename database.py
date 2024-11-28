from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, sessionmaker


DB_HOST = "localhost"  # данные для подключения к бд
DB_PORT = 5433
DB_USER = "postgres"
DB_PASS = "postgres"
DB_NAME = "postgres"

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"  # т.е. используем асинхронные подключения к дб

engine = create_async_engine(DATABASE_URL)  # создаём движок

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)  # генератор сессий(транзакций)

class Base(DeclarativeBase):  # нужен для миграций
    pass







