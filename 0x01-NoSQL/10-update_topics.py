#!/usr/bin/env python3
"""
A module containing a python function update_topics
"""


def update_topics(mongo_collection, name, topics):
    """A function update_topics that updates collection topics by name"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
