# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        level_order_arr = []

        q = deque([root])

        while q:
            res = []
            for i in range(len(q)):
                
                node = q.popleft()
                res.append(node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            avg_res = sum(res)/len(res)
            level_order_arr.append(avg_res)

        return level_order_arr
