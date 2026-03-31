class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        Explanation:
        every number has 2 choices, either to consider or to not consider
        so for [1, 2, 3...n]

        1 has 2 choices
        2 has 2 choices
        3 has 2 choices

        so 2 * 2 * 2 number of subsets which is 2^n
        but 2^n will tell you the number of subsets that can be formed

        NOTE: We cannot have duplicates here meaning [1,2] is not same as [2,1] as it is not permutations

        In below Tree Diagram, You can see it shows that left branch considers picking the number, right node doesn't 
            Level 0:
                                    []

            Level 1 (decision on 1):
                            /                \
                        [1]                   []

            Level 2 (decision on 2):
                    /      \                 /      \
                [1,2]     [1]               [2]      []

            Level 3 (decision on 3):
                /   \       /   \         /   \      /   \
            [1,2,3] [1,2] [1,3] [1]    [2,3]  [2]    [3]   []

        Time complexity n * 2^n
        '''

        res = []

        subset = []

        def dfs(i): #i represents the current number index
            if i == len(nums):
                res.append(subset.copy()) #we add the 'subset' to 'res' as soon as we exhaust/iterate throughout the list
                return
            
            #decision to include nums[i] #Left Branch in the diagram
            subset.append(nums[i])
            dfs(i+1)

            #decision NOT to include nums[i] #Right Branch in the diagram
            subset.pop() #we pop whatever we appended above
            dfs(i+1)
        
        dfs(0)
        return res
