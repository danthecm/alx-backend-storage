#!/usr/bin/env python3
"""Print info in a collection"""
from pymongo import MongoClient
""" Make a check for all elements in a collention """

if __name__ == "__main__":
    # Connect to the MongoDB
    client = MongoClient('mongodb://localhost:27017')
    db = client['logs']
    collection = db['nginx']

    # Count the total number of documents
    total_logs = collection.count_documents({})

    # Count the number of documents with different methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {
        method: collection.count_documents(
            {"method": method}) for method in methods
        }

    # Count the number of documents with method=GET and path=/status
    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"})

    # Print the statistics
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"    method {method}: {method_counts[method]}")
    print(f"{status_check} status check")

    # Close the MongoDB connection
    client.close()
