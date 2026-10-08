# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 2 binary trees 

        # traverse the root tree
        # recursively: 
        # if there is a node === root of the subroot tree
        #.   this is one function 
        # check if the trees are equal
        #.   this is another function 

        # dfs 

        # return true if subroot is in root 

        # return false otherwise
        
        def isSameTree(a, b): 
            # if they are both null, then true 
            # that means that happy ending, they both end at the same time
            if not a and not b: 
                return True 

            # if one of them is null, then mismatch 
            # this is because that means they didnt get to finish at the same time
            if not a or not b: 
                return False

            # if the values are not the same, then mismatch
            if a.val != b.val: 
                return False 

            # if the pairs match, then we need to recursively check if the rest of the trees match 
            # this line checks the right and left subtrees 
            return isSameTree(a.left, b.left) and isSameTree(a.right, b.right)
            
        
        def dfs(curr): 
            if not curr: 
                return False 

            if isSameTree(curr, subRoot): 
                return True 
            
            # this is or because any location is ok, we don't care where the root is
            # we just want to make sure they exist in both trees
            return dfs(curr.left) or dfs(curr.right)
        
        return dfs(root)

            
