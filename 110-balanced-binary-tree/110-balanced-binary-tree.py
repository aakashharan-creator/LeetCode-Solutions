# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        bal, _ = self.rec(root)
        return bal

    def rec(self, root):
        if not root:
            return (True, 0)
        
        left_bal, left_depth = self.rec(root.left)
        right_bal, right_depth = self.rec(root.right)
        
        if not left_bal or not right_bal:
            return (False, -1)
        
        if abs(left_depth - right_depth) > 1:
            return (False, -1)
        
        return (True, 1 + max(left_depth, right_depth))