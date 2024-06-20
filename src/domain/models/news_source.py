from .source import Source

import aiohttp
from rss_parser import RSSParser
from rss_parser.models import XMLBaseModel


class NewsSource(Source):
    rss: XMLBaseModel
    rss_url: str

    def __init__(self, name: str, rss_url: str):
        super().__init__(name=name)
        self.rss_url = rss_url
        self.upload_rss_()

    async def upload_rss_(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.rss_url) as response:
                self.rss = RSSParser.parse(await response.text())
