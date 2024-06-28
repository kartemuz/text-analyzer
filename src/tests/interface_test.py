import asyncio

from src.interface.controllers import (
    StoreController,
    AnalyzerController,
    UserController,
    NewsSourceController,
    UserSessionController
)


async def main():
    login = 'ivan'
    password = 'qwerty'

    await StoreController.create_store()
    user_controller = UserController()
    news_source_controller = NewsSourceController()
    await user_controller.create_default()
    await news_source_controller.create_default()
    #
    # analyzer_controller = AnalyzerController()
    # user_controller = UserController()
    # user = await user_controller.get(login, password)
    # links_dict = await analyzer_controller.search(user)
    # for tag in links_dict.keys():
    #     print(tag)
    #     for link in links_dict[tag]:
    #         print(link)
    #     print()
    
    login = 'ivan'
    password = 'qwerty'
    session = await UserSessionController(login, password).create()
    response = await session.search()
    for tag in response.keys():
        print(tag)
        for t in response[tag]:
            print(t)
        print()
    del session


if __name__ == '__main__':
    asyncio.run(main())
