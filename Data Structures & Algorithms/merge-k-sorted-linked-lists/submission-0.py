# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sortedList = None
        for i in range(len(lists)):
            sortedList = self.mergeLists(sortedList, lists[i])
        return sortedList

    def mergeLists(self, list1, list2):
        dummy = ListNode(0)
        pointer = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                pointer.next = list1
                list1 = list1.next
            else:
                pointer.next = list2
                list2 = list2.next
            pointer = pointer.next
        
        if list1:
            pointer.next = list1
        else:
            pointer.next = list2
        return dummy.next
