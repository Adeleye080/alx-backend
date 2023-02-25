#!/usr/bin/env python3
from base_caching import BaseCaching
"""LRUCache module
"""


class LRUCache(BaseCaching):
    """ Least Recently Used caching system """
    def __init__(self):
        """ initializes class attribute and superclass """
        super().__init__()
        recency = []

    def put(self, key, item):
        """ adds new data to cache
        using LRU algorithm to maintain cache size """
        if key is None or item is None:
            pass
        if BaseCaching.MAX_ITEMS <= len(self.cache_data):
            print("DISCARD: {}".format(self.recency[0]))
            del self.cache_data[self.recency[0]]
            del self.recency[0]
        self.item_order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ return value im cache linked to key """
        if key in self.recency:
            del self.recency[self.recency.index(key)]
        self.recency.append(key)
        if key is not None:
            return self.cache_data[key]
        else: None