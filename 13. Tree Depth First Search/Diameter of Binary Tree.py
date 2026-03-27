# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_len = -1

        def dfs(root):
            nonlocal max_len
            if not root:
                return 0

            left_height = dfs(root.left)
            right_height = dfs(root.right)

            total_height = left_height + right_height
            max_len = max(total_height,max_len)
            
            return max(left_height,right_height) + 1
        
        dfs(root)
        return max_len
