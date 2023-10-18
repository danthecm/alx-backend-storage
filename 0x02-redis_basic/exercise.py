#!/usr/bin/env python3
"""Exercise for Redis Basics"""
import redis
import uuid
from typing import Union


class Cache:
    def __init__(self) -> None:
        """Initialize Redis and flush it"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis using a random key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
