class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        #Solution 1: Used subsets I idea for it and used set() to remove the duplicates and it works
        # res = set()

        # subsets = []

        # def dfs(i):
        #     if i == len(nums):
        #         res.add(tuple(subsets.copy()))
        #         return

        #     #include the number
        #     subsets.append(nums[i])
        #     dfs(i+1)

        #     #do not include the number
        #     subsets.pop()
        #     dfs(i+1)
        
        # dfs(0)
        # return [list(x) for x in res]

        #### Solution 2: Cleaner Optimal Way
        '''
        - Intuition: As there can be multiple duplicate numbers:
        - We already know for right branch (not considering the number), we skip the current number. But as we have duplicates, we need to not only skip the number but make sure we skip all the duplicate numbers comes right after the current number. 
        - As the array wont be sorted, we will sort the array and then whenever we need to skip the curr number, we  just compare it to next number and if both are same, we keep skipping
        - Tree Diagram
        Level 0:
                                []

        Level 1 (index 0 → 1)
                            /                \
                        [1]                []

        --------------------------------------------------

        Level 2 (index 1 → first 2)

        From [1]:
                    /         \
                [1,2]         [1]

        From []:
                    /         \
                [2]          []

        ⚠️ NOTE:
        - We DO NOT take the second '2' here directly at same level
        - Only first '2' is allowed at this level

        --------------------------------------------------

        Level 3 (index 2 → second 2)

        From [1,2]:
                /          \
            [1,2,2]       [1,2]

        From [1]:
                /          \
                [1,2]        [1]

        From [2]:
                /          \
                [2,2]        [2]

        From []:
                ❌ SKIPPED duplicate branch
                (second 2 ignored at same level)

        --------------------------------------------------

        Level 4 (index 3 → 3)

        From [1,2,2]:
            /         \
        [1,2,2,3]   [1,2,2]

        From [1,2]:
            /         \
        [1,2,3]     [1,2]

        From [1]:
            /         \
        [1,3]       [1]

        From [2,2]:
            /         \
        [2,2,3]     [2,2]

        From [2]:
            /         \
        [2,3]       [2]

        From []:
            /         \
            [3]         []
        '''

        res = []
        subset = []
        nums.sort()

        def backtrack(i):
            if i == len(nums):
                res.append(subset.copy())
                return

            # All subset that include nums[i]
            subset.append(nums[i])
            backtrack(i+1)
            subset.pop()

            #All subset that does not include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1 #After the while loop breaks, it will point to the last duplicate
            backtrack(i+1)

        backtrack(0)
        return res
