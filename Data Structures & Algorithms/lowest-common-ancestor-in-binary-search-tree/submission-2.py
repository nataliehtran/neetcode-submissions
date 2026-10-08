# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # we know that p and q will never be the same and they will always exist 

        #.  p and q are children of the node 
        #.  p or q is the parent of the other 

        # theres a split between the nodes for right and left, then the root is the lca 
        # if both are on the right side, we can just go to the right subtree

        cur = root # start at the root

        while cur: # keep it running until we find the result 
            if p.val > cur.val and q.val > cur.val: 
                cur = cur.right 
            elif p.val < cur.val and q.val < cur.val: 
                cur = cur.left 
            # this is the case that 
            # 1. one is smaller and the other is bigger
            # 2. one of them is = to cur 
            else: 
                return cur 
