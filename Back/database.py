from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = 'postgresql://postgres:1234@localhost:5432/PlayTest'
engine = create_async_engine(url = DATABASE_URL, echo = True)

class Base(DeclarativeBase):
    pass