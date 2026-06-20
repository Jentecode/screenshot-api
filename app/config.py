from pydantic_settings import BaseSettings, SettingsConfigDict


#https://pydantic.dev/docs/validation/latest/concepts/pydantic_settings/#dotenv-env-support
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    API_KEYS: str
    REDIS_URL: str
    CACHE_TTL: int


settings = Settings() 
# gebruik om te importeren in andere map, bv
# from app.config import settings
# settings.REDIS_URL