import asyncio

from src.interface.controllers import StoreController


async def main():
    await StoreController.create_store()


if __name__ == '__main__':
    asyncio.run(main())
