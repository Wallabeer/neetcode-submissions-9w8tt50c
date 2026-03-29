# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        if not (root and subRoot):
            return False

        if self.isSame(root, subRoot):
            return True
        else:
            leftValid = self.isSubtree(root.left, subRoot)
            rightValid = self.isSubtree(root.right, subRoot)
            return leftValid or rightValid
    
    def isSame(self, node1, node2):
        if not node1 and not node2:
            return True
        
        if not (node1 and node2):
            return False
        
        if node1.val == node2.val:
            leftValid = self.isSame(node1.left, node2.left)
            rightValid = self.isSame(node1.right, node2.right)
            return leftValid and rightValid
        else:
            return False

            