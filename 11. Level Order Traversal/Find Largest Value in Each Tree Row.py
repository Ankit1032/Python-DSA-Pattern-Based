# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        # My Solution [WORKS but this is not level order traversal, It is DFS]
        # Using a hashmap where key is level and value is the largest value in that level
        
        # level_map = {}
        
        # def level_order(root, level=0):
            
        #     if not root:
        #         return
            
        #     level_map[level] = max(root.val, level_map.get(level,float('-inf')))

        #     level_order(root.left, level+1)
        #     level_order(root.right, level+1)

        # level_order(root, 0)

        # arr_val = [0] * len(level_map.keys())

        # for i in range(len(arr_val)):
        #     arr_val[i] = level_map[i]

        # return arr_val

        ### NEETCODE - USING LEVEL ORDER TRAVERSAL
        if not root:
            return root
        res = []

        q = deque([root])

        while q:
            row_max = float('-inf')
            for _ in range(len(q)):
                node = q.popleft()
                row_max = max(node.val,row_max)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(row_max)
        
        return res

