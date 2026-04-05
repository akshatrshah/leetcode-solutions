# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def func(node):
            if not node:
                return 0
            depth = 1 + max(func(node.left),func(node.right))
            return depth
        
        res = 0
        
        if not root:
            return 0
        diameter = func(root.left) + func(root.right)
        return max(diameter,self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
        

