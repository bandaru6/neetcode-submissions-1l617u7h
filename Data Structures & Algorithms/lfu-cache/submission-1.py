from collections import defaultdict

class Node:
    def __init__(self, key = 0, val = 0, freq = 0, prev = None, nxt = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = nxt
        self.freq = freq

class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def insert(self, node):
        prev = self.tail.prev
        prev.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = prev
        self.size += 1

    def remove(self, node):
        
        temp = node.prev
        node.prev.next = node.next
        node.next.prev = temp
        self.size -= 1


class LRUCache:
    def __init__(self, capacity: int):
        
        self.order = LinkedList()
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.order.remove(self.cache[key])
        self.order.insert(self.cache[key])
        return self.cache[key].val
    
    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.order.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.order.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            delete = self.order.head.next
            self.order.remove(delete)
            del self.cache[delete.key]

class LFUCache:

    def __init__(self, capacity: int):
        
        
        self.freqMap = defaultdict(LinkedList) #freq -> linked list
        self.cache = {} #key -> node
        self.capacity = capacity
        self.minFreq = 0

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        self.freqMap[self.cache[key].freq].remove(self.cache[key])

        if self.minFreq == self.cache[key].freq and self.freqMap[self.cache[key].freq].size == 0:
            self.minFreq +=1

        self.cache[key].freq += 1

        self.freqMap[self.cache[key].freq].insert(self.cache[key])

        return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key not in self.cache:
            self.cache[key] = Node(key, value, 1)
        else:
            freq = self.cache[key].freq
            self.freqMap[freq].remove(self.cache[key])

            if freq == self.minFreq and self.freqMap[freq].size == 0:
                self.minFreq += 1

            self.cache[key].freq += 1
            self.cache[key].val = value

        if len(self.cache) > self.capacity:
            delete = self.freqMap[self.minFreq].head.next
            self.freqMap[self.minFreq].remove(delete)
            del self.cache[delete.key]
        
        if self.cache[key].freq == 1:
            self.minFreq = 1
        
        self.freqMap[self.cache[key].freq].insert(self.cache[key])

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)