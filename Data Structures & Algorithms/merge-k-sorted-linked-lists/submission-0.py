# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        big = []
        for l in lists:
            
            while l:
                big.append(l.val)
                l = l.next
        big.sort()
        dummy = ListNode()
        res = dummy
        for x in big:
            dummy.next = ListNode(x, None)
            dummy = dummy.next
        
        return res.next