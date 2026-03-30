import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # #There can be duplicate x,y points so we cannot use dictionary

        # def euclid_calc(x,y):
        #     distance = math.sqrt((x*x) + (y*y))
        #     return distance
        
        # # euclid_dict = {}
        # # for i,j in points:
        # #     euclid_dict[(i,j)] = euclid_calc(i,j)

        # euclid_list = []
        # for x, y in points:
        #     euclid_list.append((euclid_calc(x, y), [x, y]))
        
        # # sort based on distance
        # euclid_list.sort(key=lambda p: p[0])
        
        # return [point for _, point in euclid_list[:k]]

        # Solution 2: Max Heap (As python only supports min heap, we will make distance as negative)
        heap = []
        
        for x, y in points:
            dist = x*x + y*y
            
            heapq.heappush(heap, (-dist, [x, y]))
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [point for dist, point in heap]
