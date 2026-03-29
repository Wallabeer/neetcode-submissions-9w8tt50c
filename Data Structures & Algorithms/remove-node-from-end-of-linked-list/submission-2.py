# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer = head
        for _ in range(n):
            pointer = pointer.next
        
        dummy = ListNode(0, head)
        root = dummy
        while pointer:
            pointer = pointer.next
            root = root.next

        if root.next:
            root.next = root.next.next
        
        return dummy.next

        
            