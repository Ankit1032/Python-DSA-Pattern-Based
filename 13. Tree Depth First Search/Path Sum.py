# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        # even the below wont work as we need to make sure the this is leaf, this might not be leaf, it will be simple we are add node.left where it is null whereas the parent node might contain root.right
        # if not root:
        #     return False
        
        #DFS
        def dfs(root,sum_path):
            if not root:
                return False

            #I was using the below code before and its wrong because the question says only return true if all nodes from root to leaf add upto target. 
            # if sum_path == targetSum:
            #     return True


            sum_path += root.val

            #This checks if the node is actually leaf node only
            if not root.left and not root.right:
                return sum_path == targetSum
                
            left_flag = dfs(root.left,sum_path)
            right_flag = dfs(root.right,sum_path)

            return left_flag or right_flag
        
        return dfs(root,0)
