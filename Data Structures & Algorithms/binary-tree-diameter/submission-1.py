# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = 0

        def dfs(curr): 
            if not curr: 
                return 0

            left = dfs(curr.left) # this is the height of the subtree
            right = dfs(curr.right)


            nonlocal diameter 
            diameter = max(diameter, left+right)
            return 1 + max(left, right) # this is the height of the subtree


        dfs(root)
        return diameter