class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        #Intuition is same as Merge Intervals Code 
        #But here I am just tracking the intersection and appeding it in a list
        intervals = []
        intervals = firstList + secondList
        

        intervals = sorted(intervals, key = lambda x : x[0])

        result = []
        prevEnd = intervals[0][1]

        for start,end in intervals[1:]:

            #overlap/intersection
            if prevEnd >= start:
                result.append([start, min(prevEnd,end)])
                prevEnd = max(prevEnd,end)
            else:
                prevEnd = end
            

        return result
