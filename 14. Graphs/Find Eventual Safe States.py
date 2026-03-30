class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        #My solution [DOES NOT WORK] , because i m only checking immediate nodes which are connected to terminal nodes
        #but questions says safe nodes are those whose all path eventually lead to terminal node
        # graph_dict = {}

        # for i in range(len(graph)):
        #     graph_dict[i] = graph[i]

        # print("graph_dict: ",graph_dict)

        # #Terminal Node
        # term_arr = []

        # for k,v in graph_dict.items():
        #     if v == []:
        #         term_arr.append(k)

        # #safe node
        # safe_node = []
        # for k,v in graph_dict.items():
        #     if v != []:
        #         flag = True
        #         for i in v:
        #             #print(k,i)
        #             if i not in term_arr:
        #                 flag = False
        #         if flag:
        #             safe_node.append(k)
        
        # print("terminal: ",term_arr)
        # print("safe: ",safe_node)

        # return sorted(term_arr + safe_node)

        #### SOLUTION 2 ####
        n = len(graph)
        safe = {} #we will capture all nodes and label if they are sfae or not

        def dfs(i):

            if i in safe: #means that node is visisted and safe has the label
                return safe[i]
            
            safe[i] = False #initially, we assume the node is not safe node, so we can find all its cycles

            #Detecting Cycle
            for neighbour in graph[i]:
                print(i)
                if not dfs(neighbour):
                    return False
            
            safe[i] = True
            return True



        res = []
        for i in range(n):
            if dfs(i): #if the nodes are safe
                res.append(i) #as we are looping from 0 to n-1, we dont need to sort the array (question has asked to show the output sorted)
        
        return res

        '''
    Intuition:
        There can be only 2 cases:
        1. If any node/path leads to a cycle → NOT safe ❌
        2. If all paths end safely → SAFE ✅

    But instead of asking: "Is there a cycle?"
    You are asking: "Does this node eventually reach a cycle?"

    safe[i] = False --> meaning "I am currently exploring this node, assume it's unsafe unless proven otherwise."

    What happens during DFS?
        CASE 1 : You revisit a node already marked False
            You are currently exploring it
            You came back → cycle detected

            So, return False

        Case 2: All neighbors are safe
            if -->
            for neighbour in graph[i]:
                if not dfs(neighbour):
                    return False
            
        This means:
            1. If any neighbor is unsafe → I am unsafe
            
            2. If all neighbors are safe → I am safe
                then safe[i] = True

         so if a node is not part of cycle or doesn't reach cycle then it will reach terminal and will be a safe node
        
        Example:
        1. No Cycle: [[1],[2],[3],[4],[]]
            a. dfs(0) → dfs(1) → dfs(2) → dfs(3) → dfs(4)
            b. 4 won't enter the for loop as there is no neighbour, so it will get safe[4] = True and return True
            c. This will simultaneously make 3,2,1 as True
            d. Output: [0,1,2,3,4]

        2. Cycle:
            a. graph = {
                0: [1],
                1: [2],
                2: [3],
                3: [1],  # cycle here
                4: []
                }
            
            b. dfs(0)
                goes to 1 → 2 → 3 → 1 again
                cycle detected ❌
            
            c. safe[0] = False
                safe[1] = False
                safe[2] = False
                safe[3] = False
            
            d. dfs(4)
                no neighbors → safe ✅
                safe[4] = True
            
            e. Output: [4]

        '''

