# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        def helper(node):
            if not node:
                return None

            if node.left:
                val = helper(node.left)
                if val:
                    return val

            if self.count < k:
                self.count = self.count + 1
            if self.count == k:
                return node.val
            if node.right:
                val = helper(node.right)
                if val:
                    return val
            return None

        return helper(root)