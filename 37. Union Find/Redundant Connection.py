class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # Using union find algorithm : we will track parenst and rank here

        #Initially we are assigning each node as a parent of itself
        par = [i for i in range(len(edges) + 1)] # as we have n edges (not n - 1)

        rank = [1] * (len(edges) + 1) #initially we will keep rank as 1

        # Find parents: We need to find the root most parent here
        def find(n):
            p = par[n]

            #as the node can be parent of its self, so we keep this below condition
            while p != par[p]:

                #we shorten the links as we go upto the parent root (grandparent, greatgrandparent, ..)
                par[p] = par[par[p]] #Path compression
                p = par[p]

            return p
        
        # Return False if the nodes are already merged i.e. same parent
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            #if not same parent, we union them using rank
            # if rank of A > rank of B then we will make A as parent of B 
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += 1 #we increase rank based on # of children
            else:
                par[p1] = p2
                rank[p2] += 1 

            return True #meaning we succesfully union them
        
        #now we will go through all edge and call union() and find()
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2] #it is guarenteed atleast one edge will be redundant as there are N nodes and N edges. If there were no redundant edges, then the length of egdes should have been N-1

        '''
        Explanation: Union Find (Disjoint Set Union)
        # DSU Mental Model
        Think of this like friend groups:
            Initially: everyone is separate
            When you see an edge → merge groups
            If two nodes are already in the same group → ❌ cycle    

        #find()
            Finds root parent
            Applies path compression    

        #union()
            Merges two sets
            Detects cycle if already connected
        
        #Final Intuition
            You are basically doing
            "Are these two already connected?"
                - YES → return edge
                - NO → connect them

        #### Problem Understanding ####
            Redundant Connection
            🔹 Given:
            A graph with n nodes and n edges
            Initially it was a tree (no cycles)
            Then one extra edge was added
            🔹 Goal:

            👉 Return the edge that creates a cycle

        #### Core Idea ####
            A tree with n nodes has n-1 edges
            If we add one more edge → cycle forms

            👉 So we detect:

            “Which edge connects nodes that are already connected?”

        #### Step 1: Initialize DSU ####
            par = [i for i in range(len(edges) + 1)]
            rank = [1] * (len(edges) + 1)

            What this means
            | Node | Parent |
            | ---- | ------ |
            | 1    | 1      |
            | 2    | 2      |
            | 3    | 3      |
            Initially, every node is its own parent (separate group)

        #### Step 2: find(n) ####
            It finds the root parent (leader) of a node

            Path Compression (KEY IDEA) : “Skip one level and point directly to grandparent”

            Before Compression
                1 → 2 → 3 → 4
            After Compression
                1 → 2 → 4


        #### Step 3: union(n1, n2) ####
            def union(n1, n2):
                p1, p2 = find(n1), find(n2)

                if p1 == p2:
                    return False

            💡 Meaning:

            👉 If both nodes already have same root
            → they are already connected
            → adding this edge creates a cycle

        #### What is Rank?

            👉 Approximate height / size of tree

            We attach:

            Smaller tree → under bigger tree

        #### Step 4: Main Loop 
            for n1, n2 in edges:
                if not union(n1, n2):
                    return [n1, n2]

            What happens?

            For each edge:
                Try to connect nodes
                If already connected → ❌ cycle
                Return that edge

        #### Example Walkthrough ####
            Input: edges = [[1,2], [1,3], [2,3]]
            Step 1: 
                Union(1,2) → OK

            Step 2: 
                Union(1,3) → OK

            Step 3:

                Union(2,3)

                👉 find(2) = 1
                👉 find(3) = 1

                Same parent → 🚨 cycle

                👉 return [2,3]
        '''
