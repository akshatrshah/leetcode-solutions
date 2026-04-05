# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque()
        q.append((root,-float('inf')))
        res = 0

        while q:
            length = len(q)
            for i in range(length):
                node,mx = q.popleft()
                if node.val >= mx:
                    mx = node.val
                    res += 1
                if node.left:
                    q.append((node.left,mx))
                if node.right:
                    q.append((node.right,mx))
        return res
