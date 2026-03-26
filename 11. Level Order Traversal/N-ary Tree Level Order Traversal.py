from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        if not root:
            return []
        
        q = deque([root])

        level_order_arr = []
        while q:
            
            res = []

            for i in range(len(q)):
                node = q.popleft()

                res.append(node.val)

                # q.append(node.children)
                # Earlier i was appending children like above code
                #The problem was : This makes the queue contain lists instead of nodes → breaks traversal.
                #fixzxed with below code

                for child in node.children:
                    if child:
                        q.append(child)

            level_order_arr.append(res)
        
        return level_order_arr

