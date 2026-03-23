class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        #The idea is that
        #   - We sort the intervals so we can track them properly
        #   - If two intervals overlap, we remove the interval whose second position is bigger (meaning we remove the interval which ends later)
        #   - The intuition for the above is the interval which ends later has more changes of having overlap so we remove it
        
        min_intervals = 0
        intervals.sort()

        prevEnd = intervals[0][1] #the end value of the first interval
        # we keep track of end interval to check for overlaps

        for start,end in intervals[1:]:
            
            #no overlap
            if start >= prevEnd:
                prevEnd = end
            #overlap
            else:
                min_intervals += 1
                prevEnd = min(prevEnd,end)

        return min_intervals
