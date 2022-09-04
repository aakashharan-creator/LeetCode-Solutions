# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.recurse(root, p.val, q.val)
    
    def recurse(self, root, t1, t2):
        result = None
        
        if not root:
            return result
                
        if root.val == t1 or root.val == t2:
            result = root
            
        left_result = self.recurse(root.left, t1, t2)
        right_result = self.recurse(root.right, t1, t2)
        
        if not left_result:
            if not right_result:
                return result
            else:
                if not result:
                    return right_result
                else:
                    return result
        else:
            if not right_result:
                if not result:
                    return left_result
                else:
                    return result
            else:
                return root