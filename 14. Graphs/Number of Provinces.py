class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # IsConnected martix will always be a square symmetrical matrix as I believe all the edges are bidirectional, and all rows and columns denote a node

        n_of_province = 0
        n_of_nodes = len(isConnected)

        graph = defaultdict (list)

        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    graph[i].append(j)

        visited = set()

        def dfs(node):
            visited.add(node)

            for i in graph[node]:
                if i not in visited:
                    dfs(i)


        for i in range(n_of_nodes):
            if i not in visited:
                dfs(i)
                n_of_province += 1

        return n_of_province
