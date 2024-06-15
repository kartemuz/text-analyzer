import asyncio

from src.persistence.repositories import UserRepository, NewsSourceRepository
from src.domain.models import User, NewsSource


async def main():
    user = User(
        login='login1',
        password='password1',
        tags=['cats', 'dogs']
    )
    user_rep = UserRepository()
    await user_rep.add(user)
    # user.add_tag('windows')
    # await user_rep.edit(user)
    # await user_rep.delete(user.login, user.password)
    # user.add_tag('newtag')
    user.add_tag('mouse')
    await user_rep.delete(user.login, user.password)


if __name__ == '__main__':
    asyncio.run(main())
