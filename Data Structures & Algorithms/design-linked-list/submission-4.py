class Node:
    def __init__(self, val = None, nxt = None, prev = None):
        self.val = val
        self.next = nxt
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        
        if index < 0 or self.head.next == self.tail:
            return -1
        curr = self.head.next
        for i in range(index):
            curr = curr.next
            if curr == self.tail:
                return -1
        return curr.val

    def addAtHead(self, val: int) -> None:
        temp = self.head.next
        self.head.next = Node(val, temp, self.head)
        temp.prev = self.head.next

    def addAtTail(self, val: int) -> None:
        temp = self.tail.prev
        self.tail.prev = Node(val, self.tail, temp)
        temp.next = self.tail.prev
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index < -1:
            return
        curr = self.head.next
        for i in range(index):
            curr = curr.next
            if curr == self.tail.next:
                return
        temp = curr.prev
        temp.next = Node(val, curr, temp)
        curr.prev = temp.next
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return
        curr = self.head.next
        for i in range(index):
            curr = curr.next
            if curr == self.tail:
                return
        temp = curr.prev
        ahead = curr.next
        temp.next = ahead
        ahead.prev = temp
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)