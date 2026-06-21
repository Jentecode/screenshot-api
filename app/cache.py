import redis
from app.config import settings

r = redis.from_url(settings.REDIS_URL)

def get_screenshot(key):
    ophalen = r.get(key)

    return ophalen


def save_screenshot(key, data):
    r.setex(key, settings.CACHE_TTL, data) #key is TTL en value is data (screenshot bytes)
    