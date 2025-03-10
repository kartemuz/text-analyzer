import asyncio
from src.application import services
from src.persistence.repositories import UserRepository, NewsSourceRepository
from src.application.services import AnalyzerService


async def main():
    # await StoreController.create_store()
    user_service = services.UserService(store=UserRepository)
    news_source_service = services.NewsSourceService(store=NewsSourceRepository)
    # try:
    #     await user_service.create_default()
    # except exc_store.LoginNotUniqueException:
    #     pass
    #
    # try:
    #     await news_source_service.create_default()
    # except exc_store.NewsSourceNotUnique:
    #     pass

    # ns = await news_source_service.get('Московский Комсомолец')
    # print(ns.to_str)
    # ns = await news_source_service.get('РБК')
    # rss = ns.rss
    # for i in rss.channel.content.items:
    #     print(i.title)
    # print(len(rss.channel.content.items))

    user = await user_service.get(login='ivan', password='qwerty')
    analyzer_service = AnalyzerService()

    print(await analyzer_service.search(user))


if __name__ == '__main__':
    asyncio.run(main())
