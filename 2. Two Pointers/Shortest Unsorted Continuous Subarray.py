class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        #Intuition is
        # Step1: Traverse from start to end and find the minimum number where the ascending order logic keeps breaking and stroe in min
        # Step2: Traverse from end to start and find the maximum number where the descending order logic keeps breaking and store in max
        # Step3: Travese the array again from start to end, now find the index of the number which is less than min, this means we need to start sorting the array from that particular index
        #Step4: Traverse the array again from end to start, now find the index of the number which is bigger than max, this means we need to do sorting till that particular index

        min_num = float('inf')
        max_num = float('-inf')

        for i in range(1,len(nums),1):
            if nums[i] < nums[i-1]:
                min_num = min(min_num,nums[i])

        for i in range(len(nums)-2, -1, -1):
            if nums[i] > nums[i+1]:
                max_num = max(max_num, nums[i])

        l_index = -1
        r_index = -1

        for i in range(0,len(nums)):
            if min_num < nums[i]:
                l_index = i
                break

        for i in range(len(nums)-1, -1, -1):
            if max_num > nums[i]:
                r_index = i
                break
            
        print(l_index, r_index)

        if r_index == -1 and l_index == -1: #no sorting required
            return 0
        
        return r_index - l_index + 1

