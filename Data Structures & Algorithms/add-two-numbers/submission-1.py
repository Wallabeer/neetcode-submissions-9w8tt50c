# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1Pointer = l1
        l2Pointer = l2
        
        ahead = ListNode(None)
        pointer = ahead
        overflow = 0
        while l1Pointer or l2Pointer:
            if l1Pointer:
                l1val = l1Pointer.val
                l1Pointer = l1Pointer.next
            else:
                l1val = 0

            if l2Pointer:
                l2val = l2Pointer.val
                l2Pointer = l2Pointer.next
            else:
                l2val = 0
            
            val = l1val + l2val + overflow
            overflow = 0
            if val >= 10:
                val = val - 10
                overflow = 1
            pointer.next = ListNode(val)
            pointer = pointer.next

        if overflow:
            pointer.next = ListNode(1)

        return ahead.next

            
            