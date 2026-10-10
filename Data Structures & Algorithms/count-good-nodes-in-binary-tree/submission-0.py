# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # counting how many nodes surpass the prev max 

        # is this node good? 

        # udpate the max 

        # add up good nodes form both subtrees 

        def dfs(node, maxSoFar): 
            # base case
            if not node: 
                return 0

            if node.val >= maxSoFar: 
                count = 1
            else: 
                count = 0
            
            # figure out the max to pass down to the children 
            if node.val > maxSoFar: 
                newMax = node.val 
            else: 
                newMax = maxSoFar

            leftGood = dfs(node.left, newMax)
            rightGood = dfs(node.right, newMax)

            count = count + leftGood + rightGood 

            return count 

        return dfs(root, root.val)
            