from typing import List


class User:
    login: str
    password: str
    tags: List[str]

    def __init__(self, login: str, password: str, tags=[]):
        self.login: str = login
        self.password: str = password
        self.tags: List[str] = tags

    def add_tag(self, tag: str) -> None:
        self.tags.append(tag)

    def delete_tag(self, tag: str) -> bool:
        result: bool
        if tag in self.tags:
            self.tags.remove(tag)
            result = True
        else:
            result = False
        return result

    @property
    def to_str(self) -> str:
        result = f'login: {self.login}\npassword: {self.password}\ntags:{self.tags}'
        return result
