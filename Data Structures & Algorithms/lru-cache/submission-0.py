from collections import OrderedDict as ordereddict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = ordereddict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key, True)
            return self.cache[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key, True)
        else:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(False)
                self.cache[key] = value
            else:
                self.cache[key] = value
        
