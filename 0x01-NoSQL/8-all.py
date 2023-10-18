#!/usr/bin/env python3
"""A python script that contains one function to list
all documents in a mongo collection"""


def list_all(mongo_collection):
    """List all documents in a mongo collection"""
    documents = mongo_collection.find({})

    document_list = list(documents)

    return document_list
