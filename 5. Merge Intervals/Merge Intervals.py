class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals, key = lambda x : x[0])

        result = []
        result.append(intervals[0])

        for first,second in intervals[1:]:

            prev_second = result[-1][1] #the second number in the last interval

            #Overlap check : could be both partial and complete overlap
            if prev_second >= first:
                result[-1][1] = max(prev_second, second) #this will take care of both partial/complete overlap
            else: #no overlap
                result.append([first,second])

        return result
