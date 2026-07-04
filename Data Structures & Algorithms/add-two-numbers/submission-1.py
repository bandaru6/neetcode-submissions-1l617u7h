# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy1 = ListNode(None, l1)
        dummy2 = ListNode(None, l2)
        dummy1 = dummy1.next
        dummy2 = dummy2.next


        res = ListNode(None, None)
        og = res
        carry = 0
        while dummy1 and dummy2:
            add = str(dummy1.val + dummy2.val + carry)
            res.next = ListNode(add[-1], None)
            res = res.next
            if len(add) == 2:
                carry = 1
            else:
                carry = 0
            dummy1 = dummy1.next
            dummy2 = dummy2.next
        
        while dummy1:
            add = str(dummy1.val + carry)
            res.next = ListNode(add[-1], None)
            res = res.next
            if len(add) == 2:
                carry = 1
            else:
                carry = 0
            dummy1 = dummy1.next

        while dummy2:
            add = str(dummy2.val + carry)
            res.next = ListNode(add[-1], None)
            res = res.next
            if len(add) == 2:
                carry = 1
            else:
                carry = 0
            dummy2 = dummy2.next
        
        if carry:
            res.next = ListNode(1, None)

        return og.next
