import redis
from app.config import settings

r = redis.from_url(settings.REDIS_URL)

def get_screenshot(key):
    ophalen = r.get(key)

    return ophalen


def save_screenshot(key, data):
    r.set(key, data, ex=settings.CACHE_TTL) #key is TTL en value is data (screenshot bytes)