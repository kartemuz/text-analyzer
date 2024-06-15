# Представление таблиц БД в виде классов

from typing import Annotated, List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import BaseDB, engine

int_PK = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]


class UserDB(BaseDB):
    __tablename__ = 'user'
    id: Mapped[int_PK]
    login: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)

    user_tags: Mapped[List['UserTagDB']] = relationship(cascade='all, delete-orphan')


class TagDB(BaseDB):
    __tablename__ = 'tag'
    id: Mapped[int_PK]
    name: Mapped[str] = mapped_column(unique=True)

    tag_users: Mapped['UserTagDB'] = relationship(cascade='all, delete-orphan')


class UserTagDB(BaseDB):
    __tablename__ = 'user_tag'
    id: Mapped[int_PK]
    tag_id: Mapped[int] = mapped_column(ForeignKey(f'{TagDB.__tablename__}.id', ondelete="CASCADE"))
    user_id: Mapped[int] = mapped_column(ForeignKey(f'{UserDB.__tablename__}.id', ondelete="CASCADE"))

    tag: Mapped['TagDB'] = relationship()
    user: Mapped['UserDB'] = relationship()


class NewsSourceDB(BaseDB):
    __tablename__ = 'news_source'
    id: Mapped[int_PK]
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    rss_url: Mapped[str] = mapped_column(unique=True, nullable=False)


async def initialize_database() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(BaseDB.metadata.drop_all)
        await conn.run_sync(BaseDB.metadata.create_all)
