# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        #My Solution and it works great! [Solution 2 is a bit more optimal where we dont consider res]
        # Poor wording and example in this one. I believe what leetcode is saying is that we want rightmost node on every level of the tree.

        # if not root:
        #     return []
        
        # q = deque([root])
        
        # level_rightmost_node = []

        # while q:
        #     res = []
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         res.append(node.val)

        #         if node.left:
        #             q.append(node.left)

        #         if node.right:
        #             q.append(node.right)

        #     level_rightmost_node.append(res[-1])
        
        # return level_rightmost_node

        
        if not root:
            return []
        
        q = deque([root])
        result = []

        while q:
            level_size = len(q)

            for i in range(level_size):
                node = q.popleft()

                if i == level_size - 1:  # last node in level
                    result.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return result


