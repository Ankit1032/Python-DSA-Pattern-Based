class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        ##### Solution 1 - Solved using DFS ####
        # IsConnected martix will always be a square symmetrical matrix as I believe all the edges are bidirectional, and all rows and columns denote a node

        # n_of_province = 0
        # n_of_nodes = len(isConnected)

        # graph = defaultdict (list)

        # for i in range(len(isConnected)):
        #     for j in range(len(isConnected[i])):
        #         if isConnected[i][j] == 1:
        #             graph[i].append(j)

        # visited = set()

        # def dfs(node):
        #     visited.add(node)

        #     for i in graph[node]:
        #         if i not in visited:
        #             dfs(i)


        # for i in range(n_of_nodes):
        #     if i not in visited:
        #         dfs(i)
        #         n_of_province += 1

        # return n_of_province

        ### Solution 2 - Union Find DSU ####
        n = len(isConnected)

        par = [i for i in range(n)]
        rank = [1] * n
        print(par)

        def find(x):
            p = par[x]
            
            while p != par[p]:
                par[p] == par[par[p]]
                p = par[p]
            
            return p
        
        def union(n1, n2):
            root_n1 = find(n1)
            root_n2 = find(n2)

            if root_n1 == root_n2:
                return

            if rank[root_n1] > rank[root_n2]:
                par[root_n2] = root_n1
                rank[root_n1] += rank[root_n2]
            else:
                par[root_n1] = root_n2
                rank[root_n2] += rank[root_n1]

        #objective of this for loops is: “Merge all cities that are directly connected so that each group represents a province.”
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    union(i, j)

        # Count unique parents (provinces) #because each parent represents a group so each group will be a province
        provinces = len(set(find(i) for i in range(n)))
        print(par)
        return provinces


