# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: 
            return []
        
        res = []

        def dfs(root, current_sum, path):
            if not root:
                return
            
            current_sum += root.val
            path.append(root.val)

            #check leaf node
            if not root.left and not root.right:
                if current_sum == targetSum:
                    res.append(path.copy()) #path.copy() so path doesn't change for other recurvise iterations
                    
            
            dfs(root.left, current_sum, path)
            dfs(root.right, current_sum, path)

            path.pop() #backtrack

        dfs(root,0,[])

        return res

