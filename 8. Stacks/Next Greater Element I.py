class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # Intuition is we interate through nums2 and keep adding the nums1 matched element into the stack until the last element of the stack is lesser than the current element of nums2, which means the current element is the next greate r element. We use a while loop until we track all the numbers in stack which are lesser than the current element and label the current element as their next greater element.
        # You will observe that the numbers in stack gets stored in descending order because as soon as a higher number is found, it gets labelled as next greater element.  
        
        n1_hashmap = {}

        #1) We will make a hashmap out of nums1 as we will only find next greater element for nums 1
        for index in range(len(nums1)):
            n1_hashmap[nums1[index]] = index
        
        #2) monotonic stack:
        #A monotonic stack is a specialized stack data structure that maintains its elements in a continuously increasing or decreasing order. 
        #[2,1,3,4] ... stack=[2,1..] -> as soon as we iterate to 3, we see that 3 is the next greater ele of 2 and 1

        stack = []
        next_g_ele = [-1] * len(nums1)

        for i in range(len(nums2)):
            curr_ele = nums2[i]
            while stack and curr_ele > stack[-1]:
                val = stack.pop()
                idx = n1_hashmap[val]
                next_g_ele[idx] = curr_ele
            if curr_ele in n1_hashmap.keys():
                stack.append(curr_ele)
        
        return next_g_ele

                

