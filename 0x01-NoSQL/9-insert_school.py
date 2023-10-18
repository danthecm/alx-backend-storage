#!/usr/bin/env python3
"""
A module containing function insert_school
"""


def insert_school(mongo_collection, **kwargs):
    """Insert a new school into the database"""
    result = mongo_collection.insert_one(kwargs)

    return result.inserted_id
