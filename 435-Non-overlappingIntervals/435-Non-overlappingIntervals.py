class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        start= intervals[0][0]
        end= intervals[0][1]
        remove=0
        i=1
        while i < len(intervals):
            end= intervals[i-1][1]
            print(end, intervals[i][0])
            if intervals[i][0]<end:
                print("here")
                remove+=1
                intervals[i][1] = min(intervals[i][1], end)
            i+=1
        return remove