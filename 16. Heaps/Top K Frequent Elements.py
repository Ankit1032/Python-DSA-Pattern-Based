from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #Hashmap
        # '''
        # Intuition is to create a counter dict and then extract the first top K occuring elements
        # '''
        # nums_dict = defaultdict(int)

        # for i in nums:
        #     nums_dict[i] += 1

        # sorted_nums_dict = sorted(nums_dict.items(), key = lambda x: x[1], reverse=True)

        # return [i[0] for i in sorted_nums_dict[0:k]]

        #Heap
        '''
        Explanation: We will sort the min heap based on the frequency and pop the element when it is getting bigger than len K.
        nums = [1,1,1,2,2,3], k = 2

        freq_map = {1:3, 2:2, 3:1}

        Heap process:

        Push (3,1) → [(3,1)]
        Push (2,2) → [(2,2),(3,1)]
        Push (1,3) → [(1,3),(3,1),(2,2)]

        Size > k → pop (1,3)

        Final heap → [(2,2),(3,1)]
        Answer → [2,1]
        '''
        nums_dict = defaultdict(int)

        for i in nums:
            nums_dict[i] += 1
        
        min_heap = []

        for num, freq in nums_dict.items():
            heappush(min_heap, (freq,num)) #The heap is primarily sorted by frequency, then by the number.

            if len(min_heap) > k:
                heappop(min_heap)

        return [num for freq, num in min_heap]
