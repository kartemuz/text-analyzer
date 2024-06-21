import logging
from src.config import settings
from loguru import logger

logging.basicConfig(level=logging.INFO)
logger.add(f'{settings.LOG_DIR}/{settings.LOG_FILE_NAME}', format=settings.LOG_FORMAT, rotation=settings.LOG_ROTATION)
