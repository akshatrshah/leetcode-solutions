# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(root,sub):
            if not root and not sub:
                return True
            
            if not sub or not root:
                return False
        
            return root.val == sub.val and helper(root.left,sub.left) and helper(root.right,sub.right)


        if not subRoot:
            return True
        
        if not root:
            return False
        
        if helper(root,subRoot):
            return True
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
