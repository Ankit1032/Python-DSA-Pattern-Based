class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)

        intervals = sorted(intervals, key=lambda x: x[0])

        result = []
        result.append(intervals[0])

        for first, second in intervals[1:]:

            prev_second = result[-1][1]

            if prev_second>=first:

                result[-1][1] = max(prev_second,second)
            else:
                result.append([first,second])

        return result
