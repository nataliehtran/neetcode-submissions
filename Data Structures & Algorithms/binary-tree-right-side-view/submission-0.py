# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs 

        # for each level, picking the last value to be popped? 

        res = []

        q = deque([root])

        if not root: 
            return []

        while q: 
            rightSide = None 

            # freezing the for loop for only how many nodes there are in the level 
            for i in range(len(q)): 
                node = q.popleft() # going through the nodes in the level 
                if node: # if it isn't None 
                    rightSide = node # make it the right side 
                    # by the end of the for loop, it will be the right most node 
                    q.append(node.left)
                    q.append(node.right)
                    
            # now we have the right side saved, add it to the result for this level 
            if rightSide: 
                res.append(rightSide.val)

        return res 
                    