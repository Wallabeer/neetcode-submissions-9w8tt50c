# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        node = head
        lead = head.next
        while node and lead:
            if node == lead:
                return True
            node = node.next
            if lead.next:
                lead = lead.next.next
            else:
                return False

        return False
        
            