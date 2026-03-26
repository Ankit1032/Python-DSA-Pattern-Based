# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # My solution [Doesn't work as my inution was wrong]
        # [In my below code i am trying to find the max depth]
        # 1,2,4,8,16 .. so each level will have 2n nodes given 1st node is called level 1
        # so intuition is we need to count the level and then use this formula

        # if not root:
        #     return 0

        # # DFS
        # max_level = -1

        # def dfs(root, level):
        #     nonlocal max_level #to let python know that this variable is declared outside function
        #     if not root:
        #         return
            
        #     level += 1
        #     max_level = max(max_level, level)
        #     dfs(root.left, level)
        #     dfs(root.right, level)

        # dfs(root, 0)

        # return max_level*2

        ##Solution 2 - BFS
        if not root:
            return 0

        max_width = 0

        q = Deque([(root,0)]) #tracking node and index

        while q:
            level_length = len(q)
            _, first_index = q[0]

            for _ in range(level_length):
                node, index = q.popleft()
                max_width = max(max_width, index - first_index + 1)

                if node.left:
                    q.append((node.left, 2*index))
                if node.right:
                    q.append((node.right, 2*index + 1))

        return max_width   
