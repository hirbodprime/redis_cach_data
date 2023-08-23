import redis
from django.core.cache import cache

def cache_fake_data():
    r = redis.Redis(host='localhost', port=6379, db=0)
    fake_data = r.hgetall("fake_data")
    cache.set("cached_fake_data", fake_data, timeout=60)  # Cache for 1 minute
