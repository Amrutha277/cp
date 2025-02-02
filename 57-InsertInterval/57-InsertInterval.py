class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        result = []
        inserted = False  # Track if newInterval is already added

        for start, end in intervals:
            if end < newInterval[0]:
                result.append([start, end])
            elif start > newInterval[1]:
                if not inserted:
                    result.append(newInterval)
                    inserted = True  # Mark as inserted
                result.append([start, end])
            else:
                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)

        if not inserted:
            result.append(newInterval)  # Add at the end if not inserted yet

        return result

                
