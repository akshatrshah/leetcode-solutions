# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node,mn,mx):
            if not node:
                return True
            
            if mn < node.val < mx:
                return valid(node.left,mn,node.val) and valid(node.right,node.val,mx)
            else:
                return False
        
        if not root:
            return True
        
        return valid(root,-float('inf'),float('inf'))
                