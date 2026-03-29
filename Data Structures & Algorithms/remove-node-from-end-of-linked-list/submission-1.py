# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0

        pointer = head
        while count < n:
            if pointer:
                pointer = pointer.next
                count = count + 1
                print('-1-',count, pointer.val if pointer else None)

        
        if pointer is None:
            return head.next
        
        root = head
        while pointer.next:
            pointer = pointer.next
            root = root.next
            print('-2-', pointer.val, root.val)

        if root.next:
            root.next = root.next.next
        
        return head

        
            