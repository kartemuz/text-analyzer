from .source import Source

import aiohttp
from rss_parser import RSSParser
from rss_parser.models import XMLBaseModel


class NewsSource(Source):
    rss: XMLBaseModel

    async def upload_rss_(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                self.rss = RSSParser.parse(await response.text())
