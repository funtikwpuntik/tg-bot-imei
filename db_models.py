import os

from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column


# Базовый класс для декларативного описания моделей
class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(unique=True)
    api_token: Mapped[str] = mapped_column(String(64), unique=True)
    allow: Mapped[bool] = mapped_column(Boolean)

    def __repr__(self) -> str:
        # Строковое представление объекта
        return f"Users(id={self.telegram_id!r})"






# Проверка наличия файла базы данных
if not os.path.exists('database.db'):
    engine = create_engine("sqlite+pysqlite:///database.db", echo=True)  # Создание подключения к SQLite
    Base.metadata.create_all(engine)  # Создание всех таблиц, если их нет

