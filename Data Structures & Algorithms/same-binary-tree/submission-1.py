# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(a, b): 
            # if they are both null, then true 
            if not a and not b: 
                return True 

            # if one of them is null, then mismatch 
            if not a or not b: 
                return False

            # if the values are not the same, then mismatch
            if a.val != b.val: 
                return False 

            # if the pairs match, then we need to recursively check if the rest of the trees match 
            return dfs(a.left, b.left) and dfs(a.right, b.right)

            
        return dfs(p,q)
            
        
        
