# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs 

        # returning the list with the order seperated by level 

        # if tree is empty, no levels 
        if not root: 
            return []

        # result 
        res = []

        # deque and start with root node 
        q = deque([root])

        while q: 
            level = []
            for i in range(len(q)): 
                # front 
                node = q.popleft()
                # save value 
                level.append(node.val)
                # queue children 
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
            res.append(level)

        return res