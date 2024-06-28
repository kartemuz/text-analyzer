from src.domain.stores import UserStore
from ...domain import exceptions
from src.domain.models import User
from ..database.models import UserDB, TagDB, UserTagDB
from ..database.base import session_factory
from sqlalchemy import select, and_, exc
from sqlalchemy.orm import selectinload
from typing import List, Optional


class UserRepository(UserStore):
    async def get_user_db_(self, login: str, password: str) -> Optional[UserDB]:
        result: Optional[UserDB]
        async with session_factory() as session:
            query = select(UserDB).where(
                and_(
                    UserDB.login == login,
                    UserDB.password == password
                )
            )
            query_result = await session.execute(query)
            result = query_result.scalar()
        return result

    async def get_tag_db_(self, tag: str) -> Optional[TagDB]:
        result: Optional[TagDB]
        async with session_factory() as session:
            query = select(TagDB).where(TagDB.name == tag)
            query_result = await session.execute(query)
            result = query_result.scalar()
        return result

    async def get(self, login: str, password: str) -> Optional[User]:
        result: Optional[User]
        async with session_factory() as session:
            user_query = select(UserDB).options(
                selectinload(UserDB.user_tags).selectinload(UserTagDB.tag)
            ).where(
                and_(
                    UserDB.login == login,
                    UserDB.password == password
                )
            )
            user_result = await session.execute(user_query)
            user = user_result.scalar()

            result = User(
                login=user.login,
                password=user.password,
                tags=[t.tag.name for t in user.user_tags]
            )
        return result

    async def edit(self, user: User) -> bool:
        result: bool
        user_db = await self.get_user_db_(user.login, user.password)
        if user_db is not None:
            await self.delete(user.login, user.password)
            await self.add(user)
            result = True
        else:
            result = False
        return result

    async def add(self, user: User) -> None:
        async with session_factory() as session:
            user_db = UserDB(login=user.login, password=user.password)
            session.add(user_db)
            try:
                await session.commit()

            except exc.IntegrityError:
                await session.rollback()
                raise exceptions.LoginNotUniqueException(
                    message='A user with this username has already been registered',
                    extra_info={'login': user.login})

            user_db = await self.get_user_db_(login=user.login, password=user.password)

            for tag in user.tags:
                tag_db = TagDB(name=tag)
                session.add(tag_db)
                try:
                    await session.commit()
                except exc.IntegrityError:
                    await session.rollback()

                tag_db = await self.get_tag_db_(tag)

                user_tag_db = UserTagDB(user_id=user_db.id, tag_id=tag_db.id)
                session.add(user_tag_db)
                await session.commit()

    async def delete(self, login: Optional[str], password: Optional[str],
                     user: Optional[User]) -> bool:
        result: bool
        user_db: UserDB
        if user is None:
            user_db = await self.get_user_db_(login, password)
        else:
            user_db = await self.get_user_db_(user.login, user.password)
        if user_db is not None:
            async with session_factory() as session:
                await session.delete(user_db)
                await session.commit()
                result = True
        else:
            result = False
        return result

    async def get_all_logins(self) -> List[str]:
        async with session_factory() as session:
            result: List[str]
            query = select(UserDB.login)
            query_result = await session.execute(query)
            result = query_result.scalars().all()
        return result
