class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        ###### SOLUTION 1 : INDEX MARKING

        # Step 1: Push all numbers to +1 as there is a possibility number can contain 0 and we cannot ue the (multiply by -1) technique for this case
        # for i in range(len(nums)):
        #     nums[i] += 1

        # #Step 2: Mark the index of the nums negative
        # for i in range(len(nums)):
        #     index = abs(nums[i]) - 1

        #     if index == len(nums):
        #         continue
            
        #     nums[index] *= -1
        
        # #step 3: Find the positive number, as that index will be the missing number
        # num_index = -1

        # #find positive number
        # for i in range(len(nums)):
        #     if nums[i] > 0:
        #         num_index = i
        #         break

        # if num_index == -1:
        #     return len(nums)
        # return num_index


        ##### SOLUTION 2 : CYCLIC SORT
        # Cyclic Sort is an in-place sorting algorithm that efficiently sorts an array containing distinct elements within a specific, known range (typically 1 to n, or 0 to n, where n is the array's length). 
        # The key idea is to place each number at its correct, value-corresponding index by cycling elements through swaps until the entire array is sorted

        # Step 1: Swap the value to the correct index-value
        i = 0
        while i < len(nums):
            
            if nums[i] < len(nums) and nums[i] != nums[nums[i]]: #Here we aren't doing nums[nums[i] - 1] because our numbers also starts from 0
                correct = nums[i]
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1
        
        #Find the number which is not present under its index
        missing_index = -1

        for i in range(len(nums)):
            if i != nums[i]:
                missing_index = i
                break

        if missing_index == -1:
            return len(nums)
        
        return missing_index

