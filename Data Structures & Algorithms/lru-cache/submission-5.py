class Node:
    def __init__(self, val = 0, key = 0, prev = None, nxt = None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = nxt

class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert(self, val, key):
        temp = self.tail.prev
        self.tail.prev = Node(val, key, temp, self.tail)
        temp.next = self.tail.prev

    def remove(self, node):

        temp = node.prev
        temp.next = temp.next.next
        temp.next.prev = temp

class LRUCache:

    def __init__(self, capacity: int):
        
        self.capacity = capacity
        self.cache = {}
        self.order = LinkedList()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        val = self.cache[key].val
        self.order.remove(self.cache[key])
        self.order.insert(val, key)
        self.cache[key] = self.order.tail.prev

        print(self.cache[key].key, self.cache[key].val)
        return val

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.order.remove(self.cache[key])

        self.cache[key] = Node(value)
        val = self.cache[key].val

        self.order.insert(val, key)
        self.cache[key] = self.order.tail.prev

        if len(self.cache) > self.capacity:
            mkey = self.order.head.next.key
            self.order.remove(self.order.head.next)
            del self.cache[mkey]


        
