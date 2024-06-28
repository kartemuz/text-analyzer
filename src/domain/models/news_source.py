from .source import Source

import aiohttp
from rss_parser import RSSParser
from rss_parser.models.rss import RSS
from src.domain.schemas.rss import NewsSourceRSS


class NewsSource(Source):
    rss_url: str
    rss: RSS
    rss: NewsSourceRSS

    def __init__(self, name: str, rss_url: str):
        super().__init__(name=name)
        self.rss_url = rss_url

    async def create(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.rss_url) as response:
                self.rss = RSSParser.parse(await response.text(), schema=NewsSourceRSS)
        return self

    @property
    def to_str(self) -> str:
        result = f'name: {self.name}\nrss_url: {self.rss_url}\n'
        return result

    def __str__(self):
        result = self.to_str
        return result
