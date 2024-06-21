from src.domain.schemas.json import DataJson
from src.config import settings

default_data = DataJson.parse_file(settings.data_path)
