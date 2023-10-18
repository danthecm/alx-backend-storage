#!/usr/bin/env python3
"""Exercise for Redis Basics"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Count the number of times a method is called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    def __init__(self) -> None:
        """Initialize Redis and flush it"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis using a random key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self, key: str, fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float]:
        """
        Get a value from a data store using a key.
        Args:
            key (str): The key to retrieve the value.
            fn (Callable, optional): A callable function to convert
            the data to the desired format.
        Returns:
            Optional: The value associated with the key,
            optionally converted by the provided callable.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """Convert data to str"""
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Convert data to int"""
        return self.get(key, int)
