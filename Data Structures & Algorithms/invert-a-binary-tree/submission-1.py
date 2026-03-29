# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #return self.swap(root)
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left),
        return root

    #def swap(self, node):
        #if node:
        #    node.left, node.right = self.swap(node.right), self.swap(node.left),
        #return node