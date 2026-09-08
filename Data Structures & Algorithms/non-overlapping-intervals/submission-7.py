class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: x[1])
        sortIntervals = intervals
        prevEnd = sortIntervals[0][1]
        res = 0

        for i in range(1, len(sortIntervals)):
            if sortIntervals[i][0] < prevEnd:
                res += 1
                # prevEnd = min(prevEnd, sortIntervals[i][1])
            else:
                prevEnd = sortIntervals[i][1]
        return res
