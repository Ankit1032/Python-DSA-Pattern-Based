from collections import defaultdict
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
Explanation: Intuition is the question mentions its a direct acyclic graph which means there is no cycle
    - So this means it is a tree
    - Example of a Tree:
            A
           /  \
          B    C
         / \   / \
        D   E  F  G

    - Now what is the best way to reach to all node, the answer is the tree root node as it can reach to all other nodes
    - The feature which differentiates the root node from other node is that root node does not have any incoming node
    - So we will find all incoming nodes and print those nodes which have no incoming
        '''
        
        incoming = defaultdict(list)

        for src, dst in edges:
            incoming[dst].append(src)

        res = []
        for i in range(n):
            if i not in incoming.keys():
                res.append(i)
        
        return res
