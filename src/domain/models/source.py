class Source:
    rss_url: str
    name: str

    def __init__(self, rss_url: str, name: str):
        self.rss_url: str = rss_url
        self.name: str = name
