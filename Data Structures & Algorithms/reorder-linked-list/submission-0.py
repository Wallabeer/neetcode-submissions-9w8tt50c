# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slowPointer = head
        fastPointer = head.next

        while fastPointer and fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
        
        secondPointer = slowPointer.next
        slowPointer.next = None

        #reverse second part
        prev = None
        current = secondPointer
        while current:
            temp = current.next
            current.next = prev

            prev = current
            current = temp

        # merge
        firstPointer = head
        secondPointer = prev

        while secondPointer:
            firstTemp = firstPointer.next
            secondTemp = secondPointer.next

            firstPointer.next = secondPointer
            secondPointer.next = firstTemp

            firstPointer = firstTemp
            secondPointer = secondTemp