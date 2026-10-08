# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # returning true or false 
        # true: balanced, difference of height is one or less
        # false: not balanced 
        # (height of left and height of right difference) is more than one

        # track the height of left 
        # track the height of right 

        # if statement 

        # recursion that would traverse until the last node

        # base case
        if not root: 
            return True

        rightTree = root.right
        leftTree = root.left

        def dfs(curr): 
            if not curr: 
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            return 1 + max(right, left) # how many edges 

        rightHeight = dfs(rightTree)
        leftHeight = dfs(leftTree)      

        # is the difference in height more than 1?

        if ((rightHeight - leftHeight) > 1) or ((leftHeight - rightHeight) > 1) : 
            return False # not balanced tree
        else: 
            return self.isBalanced(root.left) and self.isBalanced(root.right)