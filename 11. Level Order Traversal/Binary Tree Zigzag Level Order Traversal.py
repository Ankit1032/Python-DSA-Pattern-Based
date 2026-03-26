from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # Intuition is we will track levels
        # and we use a flag to keep switching whether to paste straight or in reverse

        #BFS
        if not root:
            return []

        q = deque([root])
        level = 0
        zig_zag_arr = []
        level_flag = 1

        while q:
            res = []
            
            length = len(q)
            
            for _ in range(0,length,1):

                node = q.popleft()
                res.append(node.val)
                
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
                    
            if level_flag == 1:
                zig_zag_arr.append(res)
                level_flag = 0
            else:
                res.reverse()
                zig_zag_arr.append(res)
                level_flag = 1

        return zig_zag_arr     
                    
                   

                    
        
