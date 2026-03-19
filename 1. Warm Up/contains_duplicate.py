class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        freq_arr = {}

        for i in nums:
            if i not in freq_arr.keys():
                freq_arr[i] = 1
            else:
                return True
                #freq_arr[i] += 1
    
        return False
        
        
