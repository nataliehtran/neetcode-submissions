# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        
        # we want to check if there are right and left nodes
        # if they are null, go to the one that isn't null

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
            