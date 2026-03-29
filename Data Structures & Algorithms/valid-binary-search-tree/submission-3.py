# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, float('-inf'), float('inf'))

    def isValid(self, node, low, high):
        if not node:
            return True

        if not(node.val > low and node.val < high):
            return False
        else:
            return self.isValid(node.left, low, node.val) and self.isValid(node.right,node.val, high)