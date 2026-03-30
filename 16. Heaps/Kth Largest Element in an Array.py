from heapq import heappop, heappush
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        '''
        Intuition: using heap

        nums = [1, 2, 3, 4, 5, 6, 7, 8] 
        k = 3 so o/p will be 6 as it is the 6th largest element

        so we will start popping heap as soon as its length is greater than K
        so initially the heap will have [1, 2, 3] but then for next element
        --> add 4 --> [1, 2, 3, 4] --> >k --> pop 1 --> [2, 3, 4]
        --> add 5 --> [2, 3, 4, 5] --> >k --> pop 2 --> [3, 4, 5]
        --> add 6 --> [3, 4, 5, 6] --> >k --> pop 3 --> [4, 5, 6]
        --> add 7 --> [4, 5, 6, 7] --> >k --> pop 4 --> [5, 6, 7]
        --> add 8 --> [5, 6, 7, 8] --> >k --> pop 5 --> [6, 7, 8] 

        So now the Kth largest element will be at the 0th index of min heap
        '''
        
        min_heap = []

        for n in nums:
            heappush(min_heap, n)

            if len(min_heap) > k:
                heappop(min_heap)

        return min_heap[0]
