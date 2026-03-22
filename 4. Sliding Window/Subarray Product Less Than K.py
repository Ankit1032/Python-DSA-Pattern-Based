class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        window_product = 1
        left = 0
        sub_arr_counter = 0

        for right in range(len(nums)):

            window_product *= nums[right]

            while window_product >= k and left <= right:
                #print("enter")
                window_product //= nums[left]
                left += 1
            
            #This is the game changer logic as in a subarray [a,b,c], 
            #if its product is less than k then individually [a],[b],[c],[a,b],[b,c] prodcut also will be less than k
            # so we need to count those as well
            sub_arr_counter += (right - left + 1) 
            print(nums[left:right+1])
            print("sub_arr_counter",sub_arr_counter)
            print("=================================")
        
        return sub_arr_counter

        '''
        nums = [10,5,2,6]
        k = 100

        Dry Run:
        [10]
        sub_arr_counter 1
        =================================
        [10, 5]
        sub_arr_counter 3
        =================================
        [5, 2]
        sub_arr_counter 5
        =================================
        [5, 2, 6]
        sub_arr_counter 8
        =================================
        '''

        '''
        nums = [[10,5,2,6,3,4,8,1]]
        k = 200

        [10]
        sub_arr_counter 1
        =================================
        [10, 5]
        sub_arr_counter 3
        =================================
        [10, 5, 2]
        sub_arr_counter 6
        =================================
        enter
        [5, 2, 6]
        sub_arr_counter 9
        =================================
        [5, 2, 6, 3]
        sub_arr_counter 13
        =================================
        enter
        [2, 6, 3, 4]
        sub_arr_counter 17
        =================================
        enter
        enter
        [3, 4, 8]
        sub_arr_counter 20
        =================================
        [3, 4, 8, 1]
        sub_arr_counter 24
        =================================
        '''
