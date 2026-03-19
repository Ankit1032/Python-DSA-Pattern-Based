class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        # Solution 1
        # freq_num_dict = {}
        # pairs = 0

        # for i in nums:
        #     if i not in freq_num_dict.keys():
        #         freq_num_dict[i] = 1
        #     else:
        #         freq_num_dict[i] += 1

        # for k,v in freq_num_dict.items():

        #     if v > 1:
        #         pairs += v * (v-1)//2 #Formula devired through permutation

        # return pairs

        # Solution 2
        freq_num_dict = {}
        pairs = 0

        for i in nums:
            if i not in freq_num_dict.keys():
                freq_num_dict[i] = 1
            else:
                pairs += freq_num_dict[i]
                freq_num_dict[i] += 1

        return pairs

