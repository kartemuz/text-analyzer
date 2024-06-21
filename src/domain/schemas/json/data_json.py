from pydantic import BaseModel
from typing import List


class User(BaseModel):
    login: str
    password: str
    tags: List[str]


class NewsSource(BaseModel):
    name: str
    rss_url: str


class DataJson(BaseModel):
    news_sources: List[NewsSource]
    users: List[User]
