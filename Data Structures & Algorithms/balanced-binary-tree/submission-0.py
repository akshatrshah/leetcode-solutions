# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        if not root:
            return True

        def func(node):
            nonlocal res
            if not node:
                return 0
            
            left = func(node.left)
            right = func(node.right)
            diff = abs(left-right)
            if diff > 1:
                res = False
            
            return 1 + max(left,right)
        func(root)
        return res
            