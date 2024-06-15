from abc import abstractmethod, ABC


class Store(ABC):
    @abstractmethod
    async def create_store(self) -> None:
        pass
