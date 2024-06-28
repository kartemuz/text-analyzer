from dataclasses import dataclass


@dataclass
class AnalyzerResponse:
    source_name: str
    title: str
    link: str
    date: str

    def __str__(self):
        result = f'{self.source_name}\n{self.title}\n{self.link}\n{self.date}'
        return result
