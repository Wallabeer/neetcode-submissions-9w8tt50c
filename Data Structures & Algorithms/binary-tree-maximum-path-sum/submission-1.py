# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = root.val
        self.helper(root)
        return self.maxi

    def helper(self, node):
        if not node:
            return 0

        leftVal = max(0, self.helper(node.left))
        rightVal = max(0, self.helper(node.right))
        
        headVal = node.val + leftVal + rightVal
        self.maxi = max(self.maxi, headVal)

        return node.val + max(leftVal, rightVal)
    
