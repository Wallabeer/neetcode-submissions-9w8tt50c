"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        nodeMap = dict()
        nodes = []

        curr = head
        while curr:
            node = Node(curr.val)
            nodes.append(node)
            nodeMap[curr] = node

            curr = curr.next

        curr = head
        while curr:
            node = nodeMap.get(curr)
            node.next = nodeMap.get(curr.next)
            node.random = nodeMap.get(curr.random)
            curr = curr.next
        
        return nodes[0]


    # def copyNode(self, node):
    #     if not Node:
    #         return None

    #     copy = Node(node.val)
    #     copy.next = self.copyNode(node.next)
    #     copy.random = self.copyNode(node.random)
