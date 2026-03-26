# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        #DFS [It works]
        # level_dict = {}

        # def dfs(root, level):
        #     if not root:
        #         return

        #     level_dict[level] = root.val + level_dict.get(level, 0)
        #     dfs(root.left, level+1)
        #     dfs(root.right, level+1)

        # dfs(root, 1)

        # max_level_idx = [[float(-inf),0]] #(sum, level)
        # print(level_dict)

        # level_dict = dict(sorted(level_dict.items())) # we are doing this because if we get the max sum in initial levels, then we have to return that. If we get same max sum in any other level, we ont track that as we are supposed to return the min level with max sum.

        # for i in level_dict.keys():
        #     sum_level = level_dict[i]
        #     lvl = i

        #     if sum_level > max_level_idx[0][0]:
        #         max_level_idx[0][0] = sum_level
        #         max_level_idx[0][1] = lvl
        
        # return max_level_idx[0][1]


        # BFS 
        max_sum = float('-inf')
        curr_lvl_idx = 0
        min_lvl_idx = 0

        q = Deque([root])

        while q:
            lvl_sum = 0
            curr_lvl_idx += 1

            for i in range(len(q)):
                node = q.popleft()
                lvl_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if lvl_sum > max_sum:
                max_sum = lvl_sum
                min_lvl_idx = curr_lvl_idx

        return min_lvl_idx
