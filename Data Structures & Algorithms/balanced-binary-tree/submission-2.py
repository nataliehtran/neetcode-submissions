# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True # global variable for balanced tree 

        # perform dfs
        def dfs(curr): 
            if not curr: 
                return 0 

            left = dfs(curr.left)
            right = dfs(curr.right)

            # check the balance of the tree at this node
            if abs(left-right) > 1: 
                self.balanced = False

            return 1 + max(left, right)
    
        dfs(root)
        return self.balanced