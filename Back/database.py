from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = 'postgresql+psycopg://postgres:1234@localhost:5432/PlayTest'
engine = create_async_engine(url = DATABASE_URL, echo = True)


session_factory = async_sessionmaker(
    bind= engine,
    class_= AsyncSession,
    expire_on_commit= False
)

async def get_session():
    async with session_factory() as session:
        yield session
    
    
class Base(DeclarativeBase):
    pass