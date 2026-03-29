# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isNodeBalanced = True
        if not root:
            self.isNodeBalanced = True
        else:
            leftHeight = self.getHeight(root.left)
            rightHeight = self.getHeight(root.right)
            self.isNodeBalanced = self.isNodeBalanced and (abs(leftHeight - rightHeight) <= 1)
        return self.isNodeBalanced

    def getHeight(self, node):
        if not node:
            return 0
        else:
            leftHeight = self.getHeight(node.left)
            rightHeight = self.getHeight(node.right)
            self.isNodeBalanced = self.isNodeBalanced and (abs(leftHeight - rightHeight) <= 1)
            return 1 + max(self.getHeight(node.left), self.getHeight(node.right))