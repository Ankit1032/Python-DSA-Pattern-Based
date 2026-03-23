class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        #Solution 1 : sorting index 1 in ascending and 2 in descending
        # if not points:
        #     return 0
            
        # points.sort(key=lambda x : (x[0], -x[1]))

        # arrow_count = len(points)
        # prevEnd = points[0][1]

        # for start, end in points[1:]:

        #     if prevEnd >= start:
        #         arrow_count -= 1 #reducing arrow count as we do not require
        #         prevEnd = min(prevEnd,end) #we select min and update the prenEnd because we want to make sure that this arrow is bound to the current/smallest width of the balloon it is bursting
        #         # for example: we will use one arrow for [[1,8],[1,5],[1,4]] -> we find we will use one arrow because we keep tracking the 'end' coordinate
        #         # we will use two arrow for [[1,8],[1,5],[6,8]]
        #     else:
        #         prevEnd = end
            
        # return arrow_count

        ##### Solution 2: sorting index 1 and 2 in ascending #Better Intuition

            if not points:
                return 0

            points.sort()  # sort by start, then end

            arrows = 1
            prevEnd = points[0][1]

            for start, end in points[1:]:
                if start <= prevEnd:
                    # overlap → shrink window
                    prevEnd = min(prevEnd, end)
                else:
                    # no overlap → need new arrow
                    arrows += 1
                    prevEnd = end

            return arrows
