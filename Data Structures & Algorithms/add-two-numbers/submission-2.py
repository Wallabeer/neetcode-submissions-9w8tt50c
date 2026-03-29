# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ahead = ListNode(None)
        pointer = ahead
        overflow = 0
        while l1 or l2 or overflow:
            if l1:
                l1val = l1.val
                l1 = l1.next
            else:
                l1val = 0

            if l2:
                l2val = l2.val
                l2 = l2.next
            else:
                l2val = 0
            
            val = l1val + l2val + overflow
            overflow = 0
            if val >= 10:
                val = val - 10
                overflow = 1
            pointer.next = ListNode(val)
            pointer = pointer.next

        return ahead.next

            
            