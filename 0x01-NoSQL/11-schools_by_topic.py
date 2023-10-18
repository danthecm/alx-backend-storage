#!/usr/bin/env python3
"""A module containing a function schools_by_topics"""


def schools_by_topic(mongo_collection, topic):
    """Returns a list of all documents with topics associated"""
    documents = mongo_collection.find({'topics': topic})

    documents_list = list(documents)

    return documents_list
