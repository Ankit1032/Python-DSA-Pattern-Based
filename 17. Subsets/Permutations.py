class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        '''
        Explanation: 
        - Idea is to choose one unused number at each position


        Level 0: []

        Level 1:
            [1]       [2]       [3]

        Level 2:
        [1,2] [1,3]  [2,1] [2,3]  [3,1] [3,2]

        Level 3:
        [1,2,3] [1,3,2] [2,1,3] [2,3,1] [3,1,2] [3,2,1]


        At each step:
            - Loop through all numbers
            - Pick only those not already used
            - Backtrack after recursion

        Example Walthrough:
        nums = [1,2,3]

        1st Iteration: It will choose all numbers from the beginning : [1, 2, 3]
        2nd Iteration: It will backtrack from 3 and 3 will become unused, so later it will jump to previous iteration where 2 was selected, now 2 will be unselected, 3 will be choosen  and then in next iteration, 2 will be choosen [1, 3, 2]

        Similarly the output in order will be:
        [1, 2, 3]
        [1, 3, 2]
        [2, 1, 3]
        [2, 3, 1]
        [3, 1, 2]
        [3, 2, 1]
        '''
        
        res = []
        path = []
        used = [False] * len(nums)

        def backtrack():

            if len(path) == len(nums):
                res.append(path.copy())
                print(path)
                return

            for i in range(len(nums)):

                if used[i]:
                    continue
                
                #choose
                path.append(nums[i])
                used[i] = True

                backtrack()

                #backtrack
                path.pop()
                used[i] = False

        backtrack()
        return res

