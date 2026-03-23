class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        #Sorting Intuition (sorting 1st index in ascending and 2nd index as descending)
        #arr = [[1,2],[2,5],[1,4],[3,4],[2,8]]
        #output: [[1, 4], [1, 2], [2, 8], [2, 5], [3, 4]]


        count_removed_intervals = 0
        intervals.sort(key=lambda x: (x[0], -x[1]))

        result = []
        result.append(intervals[0])

        prevStart = intervals[0][0]
        prevEnd = intervals[0][1]

        for start,end in intervals[1:]:
            
            #complete overlap by prev indexes
            if prevStart <= start and prevEnd >= end: #prevStart <= start is redundant condition as we have already sorted so it can be removed
                count_removed_intervals += 1
            else: #no overlap/partial overlap
                prevStart = start
                prevEnd = end

        return len(intervals) - count_removed_intervals




