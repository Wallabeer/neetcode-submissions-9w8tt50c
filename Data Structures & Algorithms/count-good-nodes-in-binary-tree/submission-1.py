# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        maxi = -100
        stack = [self.isGood(root, maxi)]
        count = 0
        while len(stack) > 0:
            node, isGood, maxi = stack.pop()
            print(isGood, maxi)
            if isGood:
                count = count + 1
            if node.left:
                stack.append(self.isGood(node.left, maxi))
            if node.right:
                stack.append(self.isGood(node.right, maxi))
        return count

    def isGood(self, node, maxi):
        if node.val >= maxi:
            return node, True, node.val
        else:
            return node, False, maxi

