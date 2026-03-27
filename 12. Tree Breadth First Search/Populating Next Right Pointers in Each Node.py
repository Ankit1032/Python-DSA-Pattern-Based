from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        '''
        Question Explanation: 
               1
             /   \
            2     3
            / \   / \
           4   5 6   7

        Final Structure should be:
        Level 1:   1 -> None

        Level 2:   2 -> 3 -> None

        Level 3:   4 -> 5 -> 6 -> 7 -> None

        So internally
        2.next = 3
        4.next = 5
        5.next = 6
        6.next = 7
        '''
        if not root:
            return None
        
        q = deque([root])

        while q:
            size = len(q)

            for i in range(size):
                node = q.popleft()

                # connect to next node in queue (same level)
                if i < size - 1:
                    node.next = q[0]   # next node in same level #this code does the magic
                #intuition is until we reach to the end of the same level, each node (after popped), the next node of that node will be in q[0] as the current node is already popped
                

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root
